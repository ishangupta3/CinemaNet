import os 
import csv   
import argparse
import PIL.Image
import coremltools
import random
import time

parser = argparse.ArgumentParser(description='Use a folder of ML model classifiers to label a local unlabeled data set')
parser.add_argument('-m', '--modeldir', type=str, help='folder containing core ml models to use as labelers. Each image to label will be run through each model', default='./models', required=True)
parser.add_argument('-i', '--imagedir', type=str, help="folder containing unlabeled images to be labeled", default="./images", required=True)
parser.add_argument('-o', '--output', type=str, help="destination for labeled file containing multi labels", default="./labels", required=True)
parser.add_argument('-t', '--type', type=str, help="csv or html?", default="csv", required=False)
parser.add_argument('-pre', '--prefix', type=str, help="image url prefix, useful for adding a cloud storage provider URL for example", default="", required=False)
parser.add_argument('-l', '--limit', type=int, help="limit the number of images we label - useful for testing", default="", required=False)
parser.add_argument('-r', '--random', type=bool, help="limit the number of images we label - useful for testing", default=False, required=False)

args = parser.parse_args()

start = time.time()


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


end = time.time()

modeltime = end - start

print("")
print("Loading models took " + str(modeltime) + " seconds")
print("")

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

def html_header(): 
	html_header = """
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

	<html>

		<head>

		<title>Conforming HTML 4.01 Transitional Template</title>

		</head>

	<body>
	"""
	return html_header

def html_entry(filepath, labels):
	html_entry = """
	<div align="center" style="float:left; padding:5px; margin:5px; border:solid 1px gray;">
	<a href="finder://{}"><img src={} width="200px" /></a><br/> {}
	</div>
	"""
	del labels[0]
	filepath = os.path.normpath( os.path.join(dir_path, filepath) )
	return html_entry.format(filepath, filepath, '<br />'.join(labels) )


def html_footer():
	html_footer = """
	</body>

	</html>
	"""
	return html_footer

# open a file for writing

# for reference, for multi label we want to do
# : gs://calm-trees-123-vcm/flowers/images/5217892384_3edce91761_m.jpg,dandelion,tulip,rose
# from https://cloud.google.com/vision/automl/docs/prepare

start = time.time()

all_files = []
with open(args.output, 'wb') as writer:

	if args.type is 'csv':
 		writer = csv.writer(writer)
 	else:
 		writer.write(html_header())

	# recurse through our image directory and run inference on each image
	for subdir, dirs, files in os.walk(args.imagedir):
		for file in files:
			#print os.path.join(subdir, file)
			filepath = subdir + os.sep + file

			if filepath.endswith(".jpg"):
				all_files.append(filepath)

	#do we shuffle our files?
	if args.random is True:
		random.shuffle(all_files)

	#do we limit our file count so we can do a test run?
	if args.limit is not 0:
		all_files = all_files[:args.limit]

	for filepath in all_files:
		image = load_image(filepath, resize_to=(Width, Height))
		if image is not None:
			labels = []

			# prepend our prefix if we have it
			if args.prefix:
				labels.append( args.prefix + filepath )
			else:
				labels.append(filepath)

			for model in models:
				prediction = model.predict({'image__0': image})
				label = prediction['classLabel']
				labels.append(label)

			#write all of our predictions out to our CSV
			if args.type is 'csv':
				writer.writerow(labels)
			else:
			# write HTML label version with file name for IMG tag, etc
				writer.write( html_entry(filepath, labels) )

			print("labeled " + filepath)


if args.type is 'html':
 		writer.writer(html_footer())

end = time.time()

predictiontime = end - start

print("")
print("Completed Processing")
print("")
print( str( len(all_files) ) + " images processed in " + str(predictiontime) + " seconds")
print( str( len(all_files)/predictiontime ) + "images / second")



