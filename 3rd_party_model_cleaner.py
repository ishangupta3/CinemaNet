import os 
import argparse
import coremltools
from coremltools.models import datatypes


parser = argparse.ArgumentParser(description='Clean up a folder of ML model classifiers and fix label names, add metadata to mlmodels and fix tensor names')
parser.add_argument('-m', '--modeldir', type=str, help='folder containing core ml models to clean', default='./Models/Classifiers/3rdParty/', required=False)
parser.add_argument('-o', '--outputdir', type=str, help='folder containing core ml models to clean', default='./Models/Classifiers/Cleaned/', required=False)


args = parser.parse_args()

# load our models into our models array
dir_path = os.getcwd()

models_path = os.path.normpath( os.path.join(dir_path, args.modeldir) )
cleaned_path = os.path.normpath( os.path.join(dir_path, args.outputdir) )

print('Loading Models from: ' + models_path)



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
	
	# Update our layer names to reflect our changes above.
	for i in range(len(spec.neuralNetworkClassifier.layers)):

	    if spec.neuralNetworkClassifier.layers[i].input[0] == "sceneImage":
	        spec.neuralNetworkClassifier.layers[i].input[0] = "Image"

	    if spec.neuralNetworkClassifier.layers[i].output[0] == "sceneLabelProbs":
	        spec.neuralNetworkClassifier.layers[i].output[0] = "Scores"

	    if spec.neuralNetworkClassifier.layers[i].output[0] == "sceneLabel":
	        spec.neuralNetworkClassifier.layers[i].output[0] = "Class Label"

	# update our preprocessor input too
	spec.neuralNetworkClassifier.preprocessing[0].featureName = "Image"        


	# Update our label names
	classLabels = spec.neuralNetworkClassifier.stringClassLabels

	# for i in range(len(classLabels.vector)):
	# 	label = classLabels.vector[i]

	# 	if label in labelsToUpdateMap:
	# 		classLabels.vector[i] = labelsToUpdateMap[label]

	# 	if label == 'None_of_the_above':
	# 		classLabels.vector[i] = modelNameStripped + "_na"
		
	# 	#clean up labels for production models (not for automl)
	# 	classLabels.vector[i] = classLabels.vector[i].replace("_", ".")

	# 	# Replace any key values weve updated
	# 	for labelToReplace in labelReplaceMap:

	# 		if classLabels.vector[i].startswith(labelToReplace):
	# 			classLabels.vector[i] = classLabels.vector[i].replace(labelToReplace, labelReplaceMap[labelToReplace])

	# 	# we dont prepend our 'TLD' for labels yet.
	# 	# classLabels.vector[i] = 'synopsis.image.' + classLabels.vector[i]
				
	print(classLabels)

	model = coremltools.models.MLModel(spec)

	# # Set the model metadata
	# model.author = 'Synopsis Project - Anton Marini'
	# model.license = 'BSD'
	# model.short_description = modelNameReadable + ' Classifier'
	# model.versionString =  '1.0 Beta 1'
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

