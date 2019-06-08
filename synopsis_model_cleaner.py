import os 
import argparse
import coremltools


# Load the model
model = coremltools.models.MLModel('Models/synopsis.image.shot.angle.mlmodel')

print(model.input_description)
print(model.output_description)



spec = model.get_spec()

spec.description.input[0].name = "image"
spec.description.input[0].shortDescription = "Input image"
for label in spec.neuralNetwork.layers.stringClassLabels:
	print label

# Set the model metadata
# model.author = 'Anton Marini'
# model.license = 'BSD'
# model.short_description = '.'



# Get the interface to the model

# # Set feature descriptions manually
# model.input_description['bedroom'] = 'Number of bedrooms'
# model.input_description['bathrooms'] = 'Number of bathrooms'
# model.input_description['size'] = 'Size (in square feet)'

# # Set
# model.output_description['price'] = 'Price of the house'

# # Get the spec of the model
print(spec)

# Save the model
