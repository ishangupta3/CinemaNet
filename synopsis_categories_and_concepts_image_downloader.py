from google_images_download import google_images_download   #importing the library
from multiprocessing import Pool

# the following categories and concepts are meant to capture both general image understanding 
# as well as terminology useful to photographers, cinematographers, visual artists and those working with visual media.
# this is the beginning of a quasi 'knowledge graph', using a reverse domain labelling system
# allowing us to add labels without polluting existing label name spaces 

# due to limitations of label length in Googles Auto ML, we have removed the prefix 
#'synopsis.image.' from every cateogry and concept in this script. 

# We add those back during clean up of our CoreML models

# During training of each particular categories classifier, we also include a 'None of the above'
# label to help the system discriminate the various concepts each category contains.

# This script does *not* prune each cateogry/concept - it just helps us get a lot of images which may or may not be relevant to the concept

# This script does *not* fetch the 'None of the above' images. 

# top level dictionary key is top level category directory name 
# value is a dictionary of the concept name (sub folder) and human search terms for google image search

categories_and_concepts = {
	
	# What is the overall color saturation of the image?
	"color.saturation" : [
	{ "color.saturation.desaturated" : ["Desaturated photography", "Desaturated colors photography", "Desaturated tones photography"]},
	{ "color.saturation.muted" : ["muted photography", "muted colors photography", "muted tones photography"]},
	{ "color.saturation.neutral" : ["neutral photography", "neutral colors photography", "neutral tones photography"]},
	{ "color.saturation.pastel" : ["Pastel photography", "Pastel colors photography", "Pastel tones photography"]},
	{ "color.saturation.saturated" : ["Saturated photography", "Saturated colors photography"]},
	],

	# How do the colors in the image relate to one another?
	# do we need a `none of the above`?
	"color.theory" : [
	# contains NA when training
	{ "color.theory.analagous" : ["Analagous photography", "Analagous color photography"]},
	{ "color.theory.complementary" : ["complementary photography", "Complementary color photography"]},
	{ "color.theory.monochromatic" : ["Monochromatic photography", "Monochromatic color photography", ]},
	],

	# Overall color tone of the image
	"color.tones" : [
	# contains NA when training
	{ "color.tones.blackwhite" :  ["Black and White photography", "B&W photography"] },
	{ "color.tones.cool" : ["Cool Tones photography", "Cool colors photography"]},
	{ "color.tones.warm" : ["Warm Tones  photography", "Warm colors  photography"]},
	],

	# Is the image useful for keying?
	"color.key" : [
	# contains NA when training
	{ "color.key.luma" : ["luma key"]},
	{ "color.key.green" : ["green screen", "chroma key green"]},
	{ "color.key.blue" : ["blue screen", "chroma key blue"]},
	],

	# color.dominant is created manually

	"composition.pattern" : [
	# contains NA when training

	{ "composition.pattern.tile" : ["tiled texture", "tiled photography"]},
	{ "composition.pattern.spiral" : ["spiral texture", "spiral nature photography"]},
	# needs better search terms?
	{ "composition.pattern.reflect" : ["glide reflection pattern"]},
	{ "composition.pattern.stripe" : ["striped pattern", "stripes photography"]},
	{ "composition.pattern.spot" : ["spot texture", "spotted animal"]},
	{ "composition.pattern.fractal" : ["fractal texture", "fractal lens photography"]},
	],

	"composition.spatial" : [
 	{ "composition.spatial.perspective" : ["perspective photography", "vanishing point photography"]},
	# needs better search terms?
	{ "composition.spatial.orthographic" : ["orthographic photography", "orthographic photography"]},
	# needs better search terms?
	{ "composition.spatial.isometric" : ["isometric photography"]},
	# needs better search terms?
	{ "composition.spatial.open" : ["open composition photography",]},
	# needs better search terms?
	{ "composition.spatial.closed" : ["spot texture", "spotted animal"]},
	{ "composition.spatial.dense" : ["dense photography ", "maximalist photography"]},
	{ "composition.spatial.sparse" : ["minimal photography"]},
	{ "composition.spatial.horizon" : ["horizon", "vanishing point horizon photography"]},
	{ "composition.spatial.verticality" : ["Verticality", "Verticality photography"]},
	{ "composition.spatial.horitzontality" : ["horizontality photography -geography -geology"]},
	{ "composition.spatial.diagonality" : ["diagonality composition photography"]},
	# remove images with the fucking grid over lay ahhhhhhhh
	{ "composition.spatial.ruleofthirds" : ["rule of thirds composition photography"] },
	{ "composition.spatial.negative " : ["negative space photography"] },
	{ "composition.spatial.symmetric " : ["symmetrical photography"] },

	# sub-category
	{ "composition.spatial.centered" : ["centered composition", "centered photography"] },
    { "composition.spatial.offcentered" : ["off centered photography", "off centered composition"] },

 	],


	# train natural vs synthetic in one classifier
	"composition.texture" : [
	{ "composition.texture.natural" : ["natural texture", "organic texture"]},
	{ "composition.texture.synthetic" : ["synthetic texture", "technical texture"]},

	# train harmonious vs dissonant in one classifier
	{ "composition.texture.harmonious" : ["harmonious texture", "harmonious photography composition"]},
	{ "composition.texture.dissonant" : ["dissonant texture", "chaotic texture", "disordered photography"]},
	
	#train smooth vs rough in one classifier
	{ "composition.texture.smooth" : ["smooth texture", "smooth photography"]},
	{ "composition.texture.rough" : ["rough texture", "rough texture photography"]},

	# train cracked vs patterned (continuous?)	
	{ "composition.texture.cracked" : ["rough texture", "rough photography"]},
	{ "composition.texture.patterned" : ["pattern texture", "pattern photography"]},
	],

	
 	
 	#is the camera is angled up or down?
	"shot.angle" : [
	# contains NA when training
	{ "shot.angle.aerial" : ["aerial photography", "aerial shot"]},
	{ "shot.angle.high" : ["high angle shot", "high angle shot film"]},
	{ "shot.angle.eyelevel" : ["eye level shot", "eye level shot camera angle"]},
	{ "shot.angle.low" : ["low angle shot", "low angle shot cinematography"]},
	],
	
	# is the camera rotated about its 'z axis'? (rotated about the lens)
	"shot.level" : [
	# contains NA when training
	{ "shot.level.level" : ["level shot"]},
	{ "shot.level.tilted" : ["tilted shot", "dutch angle shot", "oblique angle shot"]},
	],

	# 
	"shot.type" : [
	# contains NA when training
	{ "shot.type.portrait" : ["portrait shot", "two shot cinematography"]},
	{ "shot.type.twoshot" : ["two shot", "eye level shot camera angle"]},
	{ "shot.type.master" : ["the master shot cinematography", "the master shot", "band photo"]},
	# Trained as a seperate concept - but still a type (ie, can have a over the shoulder two shot)
	{ "shot.type.overtheshoulder" : ["over the shoulder shot", "over the shoulder shot cinematography"]},
	],

	# how far are we from the shot subject?
	"shot.framing" : [
	{ "shot.framing.extremecloseup" : ["extreme close up shot", "extreme close up shot cinematography"]},
	{ "shot.framing.closeup" : ["close up shot", "close up shot cinematography"]},
	{ "shot.framing.medium" : ["medium shot", "medium shot cinematography"]},
	{ "shot.framing.long" : ["long shot", "long shot cinematography"]},
	{ "shot.framing.extemelong" : ["extreme long shot", "extreme long shot cinematography"]},
	],

	# is the image completely, partially or not in focus?
	"shot.focus" : [
	# contains NA when training
	{ "shot.focus.deep" : ["deep focus shot", "deep focus shot cinematography"]},
	{ "shot.focus.shallow" : ["shallow focus shot", "shallow focus shot cinematography"]},
	{ "shot.focus.out" : ["out of focus", "out of focus shot"]},
	],

	# describe the lighting environment 
	"shot.lighting" : [
	# contains NA when training
	{ "shot.lighting.soft" : ["soft lighting cinematography", "soft lighting"]},
	{ "shot.lighting.hard" : ["hard lighting cinematography", "hard lighting"]},
	{ "shot.lighting.lowkey" : ["low key lighting", "low key lighting cinematography"]},
	{ "shot.lighting.highkey" : ["high key lighting", "high key lighting cinematography"]},
	{ "shot.lighting.silhouette" : ["silhouette lighting", "silhouette lighting cinematography"]},
	],

	# what is the - generally speaking - subject of the shot, if any
	"shot.subject" : [
	# contains NA when training
	{ "shot.subject.person" : ["diverse portraits photography", "portraits of people", "people -lineart -clipart -animation"]},
	{ "shot.subject.animal" : ["wildlife photography"]},
	{ "shot.subject.object" : ["object photography", "still life photography"]},
	{ "shot.subject.text" : ["typographic design", "movie title design"]},
	{ "shot.subject.location" : ["location photography", "establishing shot"]},
	],

	# I cant figure out a better way to get diverse results :( - this feels gross - help me.
	# maybe https://www.ibm.com/blogs/research/2019/01/diversity-in-faces/ ? 
	# faces, body, bodies, limb, limbs might be too specific with the plurals? Maybe make one category?
	"shot.subject.person" : [
	{ "shot.subject.face" : ["male face", "female face", "african american face", "asian face", "old face", "diverse faces photography -collage"]},
	{ "shot.subject.body" : ["diverse human figure photography", "diverse body shapes portraits"]},
	{ "shot.subject.arms" : ["arms photography", "arms outreached photography", "arms crossed photography"]},
	{ "shot.subject.hands" : ["hands photography", "fist photography", "holding hands photography"]},
	],

	# self explanatory
	"shot.timeofday" : [
	# contains NA when training
	{ "shot.timeofday.twilight" : ["twilight time of day", "dusk", "sunset", "sunrise"]},
	{ "shot.timeofday.day" : ["midday photography"]},
	{ "shot.timeofday.night" : ["night photography"]},
	],

	# self explanatory
	"shot.weather" : [
	# contains NA when training
	{ "shot.weather.sunny" : ["Sunny weather"]},
	{ "shot.weather.cloudy" : ["Cloudy weather"]},
	{ "shot.weather.raining" : ["Rainy weather"]},
	{ "shot.weather.snowing" : ["Snowy weather"]},
	# foggy?
	# stormy?
	],

	# self explanatory
	"shot.location" : [
	# contains NA when training

	# Trained as a seperate concepts
	{"shot.location.interior" : ["Indoors", "Interior", "inside"]},
	{"shot.location.exterior" : ["Outdoors", "Exterior", "outside"]},


	# Trained as a seperate set of concept 
	{"shot.location.nature" : ["Nature"]},
	# all the building subcategories are also used
	{"shot.location.building" : ["building", "structure"]},	
	# all the 'room' subcategories are also used
	{"shot.location.room" : ["Room"]},
	# all the township sub categories are also used
	{"shot.location.township" : ["modern township -game"]},
	# all the vehicle sub categories are also used
	{"shot.location.vehicle" : ["vehicle -cartoon -toy"]},

	# all sub categories trained as a sepearate set of concepts, with their own internal 'na' categories

	# specific nature categories
	{"shot.location.nature.cave" : ["Caves"]},
	{"shot.location.nature.desert" : ["Desert"]},
	{"shot.location.nature.plains" : ["Plains"]},
	{"shot.location.nature.marsh" : ["Marsh"]},
	{"shot.location.nature.swamp" : ["Swamp"]},
	{"shot.location.nature.hillside" : ["Hillside"]},
	{"shot.location.nature.forest" : ["Forest"]},
	{"shot.location.nature.mountain" : ["Mountains"]},
	{"shot.location.nature.tundra" : ["Tundra"]},
	{"shot.location.nature.river" : ["River"]},
	{"shot.location.nature.lake" : ["Lake"]},
	{"shot.location.nature.ocean" : ["Ocean"]},
	{"shot.location.nature.canyon" : ["Canyon"]},
	{"shot.location.nature.glacier" : ["Glacier"]},
	{"shot.location.nature.sky" : ["Sky"]},
	{"shot.location.nature.space" : ["Space"]},

	# specific building categories
	{"shot.location.building.house" : ["House"]},
	{"shot.location.building.mansion" : ["Mansion"]},
	{"shot.location.building.apartment" : ["Apartment"]},
	{"shot.location.building.castle" : ["Castle"]},
	{"shot.location.building.office" : ["Office"]},
	{"shot.location.building.factory" : ["Factory"]},
	{"shot.location.building.restaurant" : ["Restaurant"]},
	{"shot.location.building.bar" : ["Bar", "pub"]},
	{"shot.location.building.cafe" : ["Cafe"]},
	{"shot.location.building.houseofworship" : ["House Of Worship"]},
	{"shot.location.building.stadium" : ["stadium"]},
	{"shot.location.building.theater" : ["theater"]},
	{"shot.location.building.garage" : ["garage"]},
	{"shot.location.building.store" : ["Store"]},
	{"shot.location.building.mall" : ["Mall"]},
	{"shot.location.building.port" : ["port", "dock", "pier"]},
	{"shot.location.building.ruins" : ["Ruins", "modern ruins"]},
	{"shot.location.building.concerthall" : ["Concert Hall"]},
	{"shot.location.building.danceclub" : ["Dance Club"]},
	{"shot.location.building.buildng.airport" : ["Airport"]},
	{"shot.location.building.station" : ["Station"]},
	{"shot.location.building.parkinglot" : ["Parking Lot"]},
	{"shot.location.building.bridge" : ["Bridge"]},
	{"shot.location.building.tunnel" : ["Tunnel"]},

	# specific room categories
	{"shot.location.room.hallway" : ["Hallway"]},
	{"shot.location.room.living" : ["Living Room"]},
	{"shot.location.room.dining" : ["Dining Room"]},
	{"shot.location.room.kitchen" : ["Kitchen"]},
	{"shot.location.room.bed" : ["Bedroom"]},
	{"shot.location.room.bath" : ["Bathroom"]},
	{"shot.location.room.closet" : ["Closet"]},
	{"shot.location.room.garage" : ["Garage"]},
	{"shot.location.room.auditorium" : ["Auditorium"]},
	{"shot.location.room.gym" : ["Gym"]},

	# specific township categories
	{"shot.location.township.city" : ["City"]},
	{"shot.location.township.town" : ["Town"]},
	{"shot.location.township.suburb" : ["Suburb"]},
	{"shot.location.township.park" : ["Park"]},
	{"shot.location.township.playground" : ["Playground"]},
	{"shot.location.township.sidewalk" : ["city sidewalk photography"]},
	{"shot.location.township.street" : ["Street"]},

	# specific vehicle categories
	{"shot.location.vehicle.car" : ["Car"]},
	{"shot.location.vehicle.bus" : ["Bus"]},
	{"shot.location.vehicle.truck" : ["Truck"]},
	{"shot.location.vehicle.train" : ["Train"]},
	{"shot.location.vehicle.boat" : ["Boat"]},
	{"shot.location.vehicle.airplane" : ["Airplane"]},
	{"shot.location.vehicle.spaceship" : ["Spaceship"]},
	],


 }

#print categories_and_classes

def download_images(arguments):
			response = google_images_download.googleimagesdownload()   #class instantiation
			paths = response.download(arguments)
			print(paths)

allArguments = []

for category_key in categories_and_concepts:
	# concepts is an array of dictionaries
	print "Category: " + category_key
	category_concepts = categories_and_concepts[category_key] 
	for concept in category_concepts:
		for concept_key in concept:
			print "Concept: " + concept_key 
			searchterms = ", ".join(concept[concept_key])
			print "Search Terms: " + searchterms

			response = google_images_download.googleimagesdownload()   #class instantiation
			arguments = { "chromedriver" : "/Users/vade/Documents/Repositories/Synopsis/CinemaNet/chromedriver", "keywords" : searchterms, "limit" : 300, "print_urls" : False, "output_directory" : "Data/download/"+category_key, "image_directory" : concept_key,  "size" : "medium", "format" : "jpg" , "no_numbering" : True }
			#arguments = { "keywords" : searchterms, "limit" : 100, "print_urls" : False, "output_directory" : "Data/download/"+category_key, "image_directory" : concept_key,  "size" : "medium", "save_source" : concept_key + "sources", "format" : "jpg" }
			allArguments.append(arguments)

# concurrent google image downloaders
pool = Pool(processes=10)
results = pool.map(download_images, allArguments)

print(results)
