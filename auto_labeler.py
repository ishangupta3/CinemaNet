import os 
import csv   
import argparse
import PIL.Image
import coremltools

parser = argparse.ArgumentParser(description='Use a folder of ML model classifiers to label a local unlabeled data set')

parser.add_argument('-m', '--modeldir', type=str, help='folder containing core ml models to use as labelers. Each image to label will be run through each model', default='./models', required=True)
parser.add_argument('-i', '--imagedir', type=str, help="folder containing unlabeled images to be labeled", default="./images", required=True)
parser.add_argument('-o', '--output', type=str, help="destination for labeled CSV file containing multi labels", default="./labels.csv", required=True)
parser.add_argument('-pre', '--prefix', type=str, help="image url prefix, useful for adding a cloud storage provider URL for example", default="", required=False)

args = parser.parse_args()


# load our models into our models array
dir_path = os.getcwd()

models_path = os.path.normpath( os.path.join(dir_path, args.modeldir) )

print('Loading Models from: ' + models_path)

models = []

for filename in os.listdir(models_path):
	if filename.endswith('.mlmodel'):	
		model_path = (os.path.join(models_path, filename))

		if model_path:
			model = coremltools.models.MLModel(model_path)

			if model:
				print('Loaded model ' + filename)
				models.append(model)
			else:
				print('Unable to load model at ' + model_path)
	else:
		continue


Height = 224 # use the correct input image height 
Width = 224 # use the correct input image width

def load_image(path, resize_to=None):

	try:
		img = PIL.Image.open(path)
		#verify apparently breaks the image!?
		# img.verify()

	except Exception:
		print('Unable to load Image' + path)
		return None

	if resize_to is not None:
		img = img.resize(resize_to, PIL.Image.ANTIALIAS)

	# ensure we pass our image as RGB - some images might be single channel or RGBA
	if img.mode != 'RGB':
		img = img.convert(mode='RGB')

	return img

# open a csv file for writing

# for reference, for multi label we want to do
# : gs://calm-trees-123-vcm/flowers/images/5217892384_3edce91761_m.jpg,dandelion,tulip,rose
# from https://cloud.google.com/vision/automl/docs/prepare

with open(args.output, 'wb') as f:
	writer = csv.writer(f)

	# recurse through our image directory and run inference on each image
	for subdir, dirs, files in os.walk(args.imagedir):
		for file in files:
			#print os.path.join(subdir, file)
			filepath = subdir + os.sep + file

			if filepath.endswith(".jpg"):
				image = load_image(filepath, resize_to=(Width, Height))

				if image is not None:
					labels = []

					# prepend our prefix if we have it
					if args.prefix:
						labels.append( args.prefix + file )
					else:
						labels.append(file)

					for model in models:
						prediction = model.predict({'image__0': image})
						label = prediction['classLabel']
						labels.append(label)

					#write all of our predictions out to our CSV
					writer.writerow(labels)
					print("labeled " + file)





