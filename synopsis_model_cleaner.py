import os 
import argparse
import coremltools

modelsToUpdate = [	
					'synopsis.image.composition.color.theory.mlmodel',
					'synopsis.image.composition.color.tones.mlmodel',
					'synopsis.image.shot.angle.mlmodel',
					'synopsis.image.shot.focus.mlmodel',
					'synopsis.image.shot.framing.mlmodel',
					'synopsis.image.shot.level.mlmodel',
					'synopsis.image.shot.type.mlmodel',
					'synopsis.image.shot.subject.mlmodel',
					'synopsis.image.shot.timeofday.mlmodel'
					# 'synopsis.interim.model.mlmodel'
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
	model = coremltools.models.MLModel('AutoML-Models/' + pathToModel)

	#print(model.input_description)
	#print(model.output_description)

	spec = model.get_spec()

	#print(spec.description)

	# spec.description.input[0].name = "image"
	# spec.description.input[0].shortDescription = "Input image"

	#print(spec)
	classLabels = spec.neuralNetworkClassifier.stringClassLabels

	for i in range(len(classLabels.vector)):
		label = classLabels.vector[i]

		# if label in labelsToUpdateMap:
		# 	classLabels.vector[i] = labelsToUpdateMap[label]

		if label == 'None_of_the_above':
			classLabels.vector[i] = modelNameStripped + "_na"
		
		#clean up labels for production models (not for automl)
		# classLabels.vector[i] = classLabels.vector[i].replace("_", ".")
		# classLabels.vector[i] = 'synopsis.image.' + classLabels.vector[i]
				
	print(classLabels)

	model = coremltools.models.MLModel(spec)

	# Set the model metadata
	model.author = 'Synopsis Project - Anton Marini'
	model.license = 'BSD'
	model.short_description = modelNameReadable + ' Classifier'
	model.versionString =  '1.0 Beta 1'
	model.save('Models/' + modelName +  '-updated.mlmodel')

	# Save the model

for model in modelsToUpdate:
	updateModel(model)

