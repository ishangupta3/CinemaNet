import os 
import argparse
import coremltools
from coremltools.models import datatypes


parser = argparse.ArgumentParser(description='Clean up a folder of ML model classifiers and fix label names, add metadata to mlmodels and fix tensor names')
parser.add_argument('-m', '--modeldir', type=str, help='folder containing core ml models to clean', default='./Models/Classifiers/AutoML/', required=False)
parser.add_argument('-o', '--outputdir', type=str, help='folder containing core ml models to clean', default='./Models/Classifiers/Cleaned/', required=False)


args = parser.parse_args()

# load our models into our models array
dir_path = os.getcwd()

models_path = os.path.normpath( os.path.join(dir_path, args.modeldir) )
cleaned_path = os.path.normpath( os.path.join(dir_path, args.outputdir) )

print('Loading Models from: ' + models_path)

# modelsToUpdate = [	
# 					# 'synopsis.image.composition.color.theory.mlmodel',
# 					# 'synopsis.image.composition.color.tones.mlmodel',
# 					# 'synopsis.image.shot.angle.mlmodel',
# 					# 'synopsis.image.shot.focus.mlmodel',
# 					# 'synopsis.image.shot.framing.mlmodel',
# 					# 'synopsis.image.shot.level.mlmodel',
# 					# 'synopsis.image.shot.type.mlmodel',
# 					# 'synopsis.image.shot.subject.mlmodel',
# 					# 'synopsis.image.shot.timeofday.mlmodel'
# 				]

# autoML labels get cliped when uploading a zip / folder and can't contain '.' separators. 
# note source AutoML models have older label names so they might not exactly match what we landed on for launch
labelsToUpdateMap = { 
					'composition_color_theory_analago' : 'composition_color_theory_analagous',
					'composition_color_theory_complem' : 'composition_color_theory_complementary',
					'composition_color_theory_monochr' : 'composition_color_theory_monochrome',
					'composition_color_tones_blackwhi' : 'composition_color_tones_blackwhite',
					}			

# Weve refactored our label names a bit, and also due to how AutoML clips labels
# we need to ensure when we run our auto_labeler.py that we get output labels that
# are within the length AutoML can handle.
# This sucks and makes it messy as hell

labelReplaceMap = {
					'composition.color' : 'color',
					'location.exterior' : 'shot.location.exterior'
}

def updateModel(originalModelFileName):

	modelName = originalModelFileName.replace('.mlmodel', '')
	modelNameStripped = modelName.replace('synopsis.image.', '').replace('.', '_')
	modelNameReadable = modelNameStripped.replace('_', ' ').title()
	# Load the model
	model = coremltools.models.MLModel(models_path + '/' + originalModelFileName)

	#print(model.input_description)
	#print(model.output_description)

	spec = model.get_spec()
	
	# print(spec)

	# Update Output names to be nicer:
	spec.description.input[0].name = "Image"
	spec.description.input[0].shortDescription = "Input image"
	spec.description.output[0].name = "Scores"
	spec.description.output[0].shortDescription = "Predicted class scores"
	spec.description.output[1].name = "Class Label"
	spec.description.output[1].shortDescription = "Predicted Class"

	spec.description.predictedFeatureName = "Class Label"
	spec.description.predictedProbabilitiesName = "Scores"
	
	# add a new output for our feature extractor (1280 array length)
	# from https://forums.developer.apple.com/thread/78876
	# nn = spec.neuralNetworkClassifier  
	# new_layer = nn.layers.add()  
	# new_layer.name = 'feature_extractor_output' #give any name here  
	# new_layer.input.append('mnas_v4_a_140_1/feature_network/feature_extractor/Mean:0') #same as the output name of the intermediate layer we want to access  
	# new_layer.output.append('feature_extractor_output') #give any name here  
	# new_layer.activation.linear.alpha = 1.0 #we add a "linear" layer with alpha==scale==1, which is an identity transformation 

	# #add a new output description  
	# new_output = spec.description.output.add()  
	# new_output.name = 'feature_extractor_output' #same name as the output of the newly added layer above  
	# new_output.shortDescription = 'Feature Vector Output'  
	# new_output_params = new_output.type.multiArrayType  
	# new_output_params.dataType = coremltools.proto.FeatureTypes_pb2.ArrayFeatureType.ArrayDataType.Value('DOUBLE')  
	# new_output_params.shape.extend([1280]) #shape should be in order [Seq, Batch, channel, height, width] or [channel, height, width]  

	# Update our layer names to reflect our changes above.



	for i in range(len(spec.neuralNetworkClassifier.layers)):

	    if spec.neuralNetworkClassifier.layers[i].input[0] == "image__0":
	        spec.neuralNetworkClassifier.layers[i].input[0] = "Image"

	    if spec.neuralNetworkClassifier.layers[i].output[0] == "scores__0":
	        spec.neuralNetworkClassifier.layers[i].output[0] = "Scores"

	    if spec.neuralNetworkClassifier.layers[i].output[0] == "classLabel":
	        spec.neuralNetworkClassifier.layers[i].output[0] = "Class Label"

	# update our preprocessor input too
	spec.neuralNetworkClassifier.preprocessing[0].featureName = "Image"        
	spec.neuralNetworkClassifier.labelProbabilityLayerName = "Scores"


	# Update our label names
	classLabels = spec.neuralNetworkClassifier.stringClassLabels

	for i in range(len(classLabels.vector)):
		label = classLabels.vector[i]

		if label in labelsToUpdateMap:
			classLabels.vector[i] = labelsToUpdateMap[label]

		if label == 'None_of_the_above':
			classLabels.vector[i] = modelNameStripped + "_na"
		
		#clean up labels for production models (not for automl)
		classLabels.vector[i] = classLabels.vector[i].replace("_", ".")

		# Replace any key values weve updated
		for labelToReplace in labelReplaceMap:

			if classLabels.vector[i].startswith(labelToReplace):
				classLabels.vector[i] = classLabels.vector[i].replace(labelToReplace, labelReplaceMap[labelToReplace])

		# we dont prepend our 'TLD' for labels yet.
		# classLabels.vector[i] = 'synopsis.image.' + classLabels.vector[i]
				
	print(classLabels)

	model = coremltools.models.MLModel(spec)

	# Set the model metadata
	model.author = 'Synopsis Project - Anton Marini'
	model.license = 'BSD'
	model.short_description = modelNameReadable + ' Classifier'
	model.versionString =  '1.0 Beta 1'
	model.save(cleaned_path + '/' + modelName +  '.mlmodel')

	# Save the model


model_paths = []

for filename in os.listdir(models_path):
	if filename.endswith('.mlmodel'):	
		model_path = filename

		if model_path:
			model_paths.append(model_path)
	else:
		continue



for model_path in model_paths:
	updateModel(model_path)

