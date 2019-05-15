# CinemaNet

CinemaNet is a set of data and trained models to help run inference to classify images / frames of a video with common Cinematography terms.

CinemaNet aims to give out of the box useful classification of images / frames of video to cinematographers, editors, archivists, and anyone interested in extracting classification in a cinema / video context.

CinemaNet also attempts to standardize other models and data sets to use a single representation for inference/classificiation. CinemaNet provides various trained models on other data sets we find useful for film/photographic classification. 

We currently standardize to a baseline MobileNet 1.0, 224 architecture - and fine tune / transfer against pre-trained Googles provided MobileNet - trained against the ImageNet database.

### Transfered Classifiers
* ImageNet Classifier - Providing out of the box ImageNet classifiers via Google's provided MobileNet.
* Places 365 classifier - Please see : Places: A 10 million Image Database for Scene Recognition B. Zhou, A. Lapedriza, A. Khosla, A. Oliva, and A. Torralba IEEE Transactions on Pattern Analysis and Machine Intelligence, 2017.


### CinemaNet Classification Categories

Classification is in progress and early stages and works more or less,  but currently consists of:

### Shot Framing
* Extreme Close Up
* Close Up
* Medium
* Long Shot
* Extreme Long Shot

### Shot Type
* Master
* Two Up
* Portrait
* Over the Shoulder

### Shot Angle
* Aerial
* High
* Straight
* Low
* Tilted

### Shot Subject
* Face
* Faces
* Person
* People
* Animal
* Text

### Requirements: 
* Tensorflow 1.5 or newer.
* Python

### Training

CinemaNet has been trained using the TF For Poets workflow using retrain.py and label_image.py.

### Contribution

Hit me up with ideas, images, or notify me of mis-labels please.

Currently exploring taxonomies for Framing, Shot Type, and Shot Angle. I want to stay away from too specific taxonomies and would rather explore more generally useful taxonomies. This is not intended to be a perfect taxonomy fit for everyone, but generally useful and an exploratory first start.

So far, I have data for Framing, need more data for Type, and have yet to delve into Angle. Current Taxonomy breakdown as follows: 

### Found Footage data sets:

Currently grabbing data from the web - citing fair use for building models. If you see your a frame you dont want me to use, please lt me know I i'll remove it. Thank you!
