from google_images_download import google_images_download   #importing the library
from multiprocessing import Pool


# top level dictionary key is top level category directory name 
# value is a dictionary of the concept name (sub folder) and human search terms for google image search

categories_and_classes = {
	"composition.color" : [
	{ "composition.color.blackwhite" :  ["Black and White photography", "B&W photography"] },
	{ "composition.color.monochromatic" : ["Monochromatic photography", "Monochromatic color photography", ]},
	{ "composition.color.analagous" : ["Analagous photography", "Analagous color photography"]},
	{ "composition.color.complementary" : ["complementary photography", "Complementary color photography"]},
	{ "composition.color.cool" : ["Cool Tones photography", "Cool colors photography"]},
	{ "composition.color.warm" : ["Warm Tones  photography", "Warm colors  photography"]},
	{ "composition.color.saturated" : ["Saturated photography", "Saturated colors photography"]},
	{ "composition.color.pastel" : ["Pastel photography", "Pastel colors photography", "Pastel tones photography"]},
	{ "composition.color.neutral" : ["neutral photography", "neutral colors photography", "neutral tones photography"]},
	{ "composition.color.muted" : ["muted photography", "muted colors photography", "muted tones photography"]},
	{ "composition.color.desaturated" : ["Desaturated photography", "Desaturated colors photography", "Desaturated tones photography"]},
	{ "composition.color.key" : ["chroma key", "luma key", "green screen", "blue screen", "alpha key"]},
	],

	"composition.texture" : [
	{ "composition.texture.natural" : ["natural texture", "organic texture"]},
	{ "composition.texture.synthetic" : ["synthetic texture", "technical texture"]},
	{ "composition.texture.harmonious" : ["harmonious texture", "harmonious photography composition"]},
	{ "composition.texture.dissonant" : ["dissonant texture", "chaotic texture", "disordered photography"]},
	{ "composition.texture.smooth" : ["smooth texture", "smooth photography"]},
	{ "composition.texture.rough" : ["rough texture", "rough texture photography"]},
	{ "composition.texture.cracked" : ["rough texture", "rough photography"]},
	{ "composition.texture.patterned" : ["pattern texture", "pattern photography"]},
	],

	"composition.pattern" : [
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
 	],

	"shot.angle" : [
	{ "shot.angle.aerial" : ["aerial photography", "aerial shot"]},
	{ "shot.angle.high" : ["high angle shot", "high angle shot film"]},
	{ "shot.angle.eyelevel" : ["eye level shot", "eye level shot camera angle"]},
	{ "shot.angle.low" : ["low angle shot", "low angle shot cinematography"]},
	{ "shot.angle.tilted" : ["tilted shot", "dutch angle shot", "oblique angle shot"]},
	],

	"shot.type" : [
	{ "shot.type.establishing" : ["establishing shot", "establishing shot cinematography"]},
	{ "shot.type.portrait" : ["portrait shot", "two shot cinematography"]},
	{ "shot.type.twoshot" : ["two shot", "eye level shot camera angle"]},
	{ "shot.type.master" : ["the master shot cinematography", "the master shot"]},
	{ "shot.type.overtheshoulder" : ["over the shoulder shot", "over the shoulder shot cinematography"]},
	],

	"shot.framing" : [
	{ "shot.framing.extremecloseup" : ["extreme close up shot", "extreme close up shot cinematography"]},
	{ "shot.framing.closeup" : ["close up shot", "close up shot cinematography"]},
	{ "shot.framing.medium" : ["medium shot", "medium shot cinematography"]},
	{ "shot.framing.long" : ["long shot", "long shot cinematography"]},
	{ "shot.framing.extemelong" : ["extreme long shot", "extreme long shot cinematography"]},
	],

	"shot.focus" : [
	{ "shot.focus.deep" : ["deep focus shot", "deep focus shot cinematography"]},
	{ "shot.focus.shallow" : ["shallow focus shot", "shallow focus shot cinematography"]},
	{ "shot.focus.out" : ["out of focus shot"]},
	],

	"shot.lighting" : [
	{ "shot.lighting.soft" : ["soft lighting cinematography", "soft lighting"]},
	{ "shot.lighting.hard" : ["hard lighting cinematography", "hard lighting"]},
	{ "shot.lighting.lowkey" : ["low key lighting", "low key lighting cinematography"]},
	{ "shot.lighting.highkey" : ["high key lighting", "high key lighting cinematography"]},
	{ "shot.lighting.silhouette" : ["silhouette lighting", "silhouette lighting cinematography"]},
	],

	"shot.subject" : [
	{ "shot.subject.person" : ["portraits of people"]},
	{ "shot.subject.people" : ["crowd of people", "people -lineart -clipart -animation", "people close together"]},
	# I cant figure out a better way to get diverse results :( - this feels gross - help me.
	# maybe https://www.ibm.com/blogs/research/2019/01/diversity-in-faces/ ? 
	{ "shot.subject.face" : ["male face", "female face", "african american face", "asian face", "old face"]},
	# faces, body, bodies, limb, limbs might be too specific with the plurals? Maybe make one category?
	{ "shot.subject.faces" : ["faces close together"]},
	{ "shot.subject.body" : ["human figure photography", ]},
	{ "shot.subject.bodies" : ["human figures photography"]},
	{ "shot.subject.limb" : ["limb body photography", "limb figure photography"]},
	{ "shot.subject.limbs" : ["limbs bodies photography" "limb figures photography"]},
	{ "shot.subject.animal" : ["wildlife photography"]},
	{ "shot.subject.object" : ["object photography", "still life photography"]},
	{ "shot.subject.text" : ["typographic design", "movie title design"]},
	{ "shot.subject.location" : ["location photography", "establishing shot"]},
	],

	"shot.timeofday" : [
	{ "shot.timeofday.twilight" : ["twilight time of day", "dusk", "sunset", "sunrise"]},
	{ "shot.timeofday.day" : ["midday photography"]},
	{ "shot.timeofday.night" : ["night photography"]},
	],

	"shot.weather" : [
	{ "shot.weather.sun" : ["Sunny weather"]},
	{ "shot.weather.clouds" : ["Cloudy weather"]},
	{ "shot.weather.rain" : ["Rainy weather"]},
	{ "shot.weather.fog" : ["Foggy weather"]},
	{ "shot.weather.snow" : ["Snowy weather"]},
	{ "shot.weather.lighting" : ["Stormy Weather"]},
	{ "shot.weather.hail" : ["Hail weather"]},
	{ "shot.weather.fire" : ["forest fire"]},
	],

	"shot.location" : [
	{"shot.location.interior" : ["Indoors", "Interior", "inside"]},
	{"shot.location.exterior" : ["Outdoors", "Exterior", "outside"]},
	{"shot.location.structure" : ["Structure", "man made"]},
	{"shot.location.nature" : ["Nature", ""]},
	{"shot.location.house" : ["House"]},
	{"shot.location.apartment" : ["Apartment"]},
	{"shot.location.mansion" : ["Mansion"]},
	{"shot.location.building" : ["Building"]},
	{"shot.location.room" : ["Room"]},
	{"shot.location.hallway" : ["Hallway"]},
	{"shot.location.livingroom" : ["Living Room"]},
	{"shot.location.diningroom" : ["Dining Room"]},
	{"shot.location.kitchen" : ["Kitchen"]},
	{"shot.location.bedroom" : ["Bedroom"]},
	{"shot.location.bathroom" : ["Bathroom"]},
	{"shot.location.closet" : ["Closet"]},
	{"shot.location.garage" : ["Garage"]},
	{"shot.location.office" : ["Office"]},
	{"shot.location.factory" : ["Factory"]},
	{"shot.location.restaurant" : ["Restaurant"]},
	{"shot.location.cafe" : ["Cafe"]},
	{"shot.location.cafeteria" : ["Cafeteria"]},
	{"shot.location.bar" : ["Bar"]},
	{"shot.location.danceclub" : ["Dance Club"]},
	{"shot.location.concerthall" : ["Concert Hall"]},
	{"shot.location.houseofworship" : ["House Of Worship"]},
	{"shot.location.store" : ["Store"]},
	{"shot.location.city" : ["City"]},
	{"shot.location.suburb" : ["Suburb"]},
	{"shot.location.village" : ["Village"]},
	{"shot.location.park" : ["Park"]},
	{"shot.location.bridge" : ["Bridge"]},
	{"shot.location.tunnel" : ["Tunnel"]},
	{"shot.location.port" : ["Port"]},
	{"shot.location.station" : ["Station"]},
	{"shot.location.parkinglot" : ["Parking Lot"]},
	{"shot.location.airport" : ["Airport"]},
	{"shot.location.playground" : ["Playground"]},
	{"shot.location.sidewalk" : ["Sidewalk"]},
	{"shot.location.street" : ["Street"]},
	{"shot.location.car" : ["Car"]},
	{"shot.location.bus" : ["Bus"]},
	{"shot.location.truck" : ["Truck"]},
	{"shot.location.train" : ["Train"]},
	{"shot.location.boat" : ["Boat"]},
	{"shot.location.airplane" : ["Airplane"]},
	{"shot.location.spaceship" : ["Spaceship"]},
	{"shot.location.cockpit" : ["Cockpit"]},
	{"shot.location.desert" : ["Desert"]},
	{"shot.location.plains" : ["Plains"]},
	{"shot.location.marsh" : ["Marsh"]},
	{"shot.location.swamp" : ["Swamp"]},
	{"shot.location.hillside" : ["Hillside"]},
	{"shot.location.forest" : ["Forest"]},
	{"shot.location.mountain" : ["Mountain"]},
	{"shot.location.tundra" : ["Tundra"]},
	{"shot.location.river" : ["River"]},
	{"shot.location.lake" : ["Lake"]},
	{"shot.location.ocean" : ["Ocean"]},
	{"shot.location.canyon" : ["Canyon"]},
	{"shot.location.glacier" : ["Glacier"]},
	{"shot.location.space" : ["Space"]},
	],

"sentiment" : [
	{ "sentiment.fear" : ["Fear photography"]},
	{ "sentiment.anger" : ["Anger photography"]},
	{ "sentiment.sadness" : ["Sadness photography"]},
	{ "sentiment.joy" : ["Joy photography"]},
	{ "sentiment.disgust" : ["Disgust photography"]},
	{ "sentiment.surprise" : ["Surprise photography"]},
	{ "sentiment.trust" : ["Trust photography"]},
	{ "sentiment.anticipation" : ["Anticipation photography"]},
	],

 }

#print categories_and_classes

def download_images(arguments):
			response = google_images_download.googleimagesdownload()   #class instantiation
			paths = response.download(arguments)
			print(paths)

allArguments = []

for category_key in categories_and_classes:
	# concepts is an array of dictionaries
	print "Category: " + category_key
	category_concepts = categories_and_classes[category_key] 
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
