import os 
import argparse
import coremltools
from coremltools.models import datatypes

modelsToUpdate = [	
					# 'synopsis.image.composition.color.theory.mlmodel',
					# 'synopsis.image.composition.color.tones.mlmodel',
					# 'synopsis.image.shot.angle.mlmodel',
					# 'synopsis.image.shot.focus.mlmodel',
					# 'synopsis.image.shot.framing.mlmodel',
					# 'synopsis.image.shot.level.mlmodel',
					# 'synopsis.image.shot.type.mlmodel',
					# 'synopsis.image.shot.subject.mlmodel',
					# 'synopsis.image.shot.timeofday.mlmodel'
					'synopsis.interim.model-2.mlmodel'
				]

# autoML labels get cliped when uploading a zip / folder and can't contain '.' separators. 
labelsToUpdateMap = { 
					'composition_color_theory_analago' : 'composition_color_theory_analagous',
					'composition_color_theory_complem' : 'composition_color_theory_complementary',
					'composition_color_theory_monochr' : 'composition_color_theory_monochrome',
					'composition_color_tones_blackwhi' : 'composition_color_tones_blackwhite',

					}			

def updateModel(pathToModel):

	modelName = pathToModel.replace('.mlmodel', '')
	modelNameStripped = modelName.replace('synopsis.image.', '').replace('.', '_')
	modelNameReadable = modelNameStripped.replace('_', ' ').title()
	# Load the model
	model = coremltools.models.MLModel('Interim Model/' + pathToModel)

	#print(model.input_description)
	#print(model.output_description)

	spec = model.get_spec()
	
	# print(spec)

	# Update Output names to be nicer:
	spec.description.input[0].name = "Image"
	spec.description.input[0].shortDescription = "Input image"
	# spec.description.output[0].name = "Scores"
	# spec.description.output[0].shortDescription = "Predicted class scores"
	# spec.description.output[1].name = "Class Label"
	# spec.description.output[1].shortDescription = "Predicted Class"

	# add a new output for our feature extractor (1280 array length)
	# from https://forums.developer.apple.com/thread/78876
	nn = spec.neuralNetworkClassifier  
	new_layer = nn.layers.add()  
	new_layer.name = 'feature_extractor_output' #give any name here  
	new_layer.input.append('mnas_v4_a_140_1/feature_network/feature_extractor/Mean:0') #same as the output name of the intermediate layer we want to access  
	new_layer.output.append('feature_extractor_output') #give any name here  
	new_layer.activation.linear.alpha = 1.0 #we add a "linear" layer with alpha==scale==1, which is an identity transformation 

	#add a new output description  
	new_output = spec.description.output.add()  
	new_output.name = 'feature_extractor_output' #same name as the output of the newly added layer above  
	new_output.shortDescription = 'Feature Vector Output'  
	new_output_params = new_output.type.multiArrayType  
	new_output_params.dataType = coremltools.proto.FeatureTypes_pb2.ArrayFeatureType.ArrayDataType.Value('DOUBLE')  
	new_output_params.shape.extend([1280]) #shape should be in order [Seq, Batch, channel, height, width] or [channel, height, width]  

	# Update our layer names to reflect our changes above.
	for i in range(len(spec.neuralNetworkClassifier.layers)):

	    if spec.neuralNetworkClassifier.layers[i].input[0] == "image__0":
	        spec.neuralNetworkClassifier.layers[i].input[0] = "Image"

	    # if spec.neuralNetworkClassifier.layers[i].output[0] == "scores__0":
	    #     spec.neuralNetworkClassifier.layers[i].output[0] = "Scores"

	    # if spec.neuralNetworkClassifier.layers[i].output[0] == "classLabel":
	    #     spec.neuralNetworkClassifier.layers[i].output[0] = "Class Label"

	# update our preprocessor input too
	spec.neuralNetworkClassifier.preprocessing[0].featureName = "Image"        


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
		classLabels.vector[i] = 'synopsis.image.' + classLabels.vector[i]
				
	print(classLabels)

	model = coremltools.models.MLModel(spec)

	# Set the model metadata
	model.author = 'Synopsis Project - Anton Marini'
	model.license = 'BSD'
	model.short_description = modelNameReadable + ' Classifier'
	model.versionString =  '1.0 Beta 1'
	model.save('Interim Model/' + modelName +  '-updated.mlmodel')

	# Save the model

for model in modelsToUpdate:
	updateModel(model)

