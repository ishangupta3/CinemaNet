from google_images_download import google_images_download   #importing the library


# top level dictionary key is top level category directory name 
# value is a dictionary of the concept name (sub folder) and human search terms for google image search

categories_and_classes = {
	"synopsis.image.composition.color" : [
	{ "synopsis.image.composition.color.blackwhite" :  ["Black and White photography", "B&W photography"] },
	{ "synopsis.image.composition.color.monochromatic" : ["Monochromatic photography", "Monochromatic color photography", ]},
	{ "synopsis.image.composition.color.analagous" : ["Analagous photography", "Analagous color photography"]},
	{ "synopsis.image.composition.color.complementary" : ["complementary photography", "Complementary color photography"]},
	{ "synopsis.image.composition.color.cool" : ["Cool Tones photography", "Cool colors photography"]},
	{ "synopsis.image.composition.color.warm" : ["Warm Tones  photography", "Warm colors  photography"]},
	{ "synopsis.image.composition.color.saturated" : ["Saturated photography", "Saturated colors photography"]},
	{ "synopsis.image.composition.color.pastel" : ["Pastel photography", "Pastel colors photography", "Pastel tones photography"]},
	{ "synopsis.image.composition.color.neutral" : ["neutral photography", "neutral colors photography", "neutral tones photography"]},
	{ "synopsis.image.composition.color.muted" : ["muted photography", "muted colors photography", "muted tones photography"]},
	{ "synopsis.image.composition.color.desaturated" : ["Desaturated photography", "Desaturated colors photography", "Desaturated tones photography"]},
	{ "synopsis.image.composition.color.key" : ["chroma key", "luma key", "green screen", "blue screen", "alpha key"]},
	],

	"synopsis.image.composition.texture" : [
	{ "synopsis.image.composition.texture.natural" : ["natural texture", "organic texture"]},
	{ "synopsis.image.composition.texture.synthetic" : ["synthetic texture", "technical texture"]},
	{ "synopsis.image.composition.texture.harmonious" : ["harmonious texture", "harmonious photography composition"]},
	{ "synopsis.image.composition.texture.dissonant" : ["dissonant texture", "chaotic texture", "disordered photography"]},
	{ "synopsis.image.composition.texture.smooth" : ["smooth texture", "smooth photography"]},
	{ "synopsis.image.composition.texture.rough" : ["rough texture", "rough texture photography"]},
	{ "synopsis.image.composition.texture.cracked" : ["rough texture", "rough photography"]},
	{ "synopsis.image.composition.texture.patterned" : ["pattern texture", "pattern photography"]},
	],

	"synopsis.image.composition.pattern" : [
	{ "synopsis.image.composition.pattern.tile" : ["tiled texture", "tiled photography"]},
	{ "synopsis.image.composition.pattern.spiral" : ["spiral texture", "spiral nature photography"]},
	# needs better search terms?
	{ "synopsis.image.composition.pattern.reflect" : ["glide reflection pattern"]},
	{ "synopsis.image.composition.pattern.stripe" : ["striped pattern", "stripes photography"]},
	{ "synopsis.image.composition.pattern.spot" : ["spot texture", "spotted animal"]},
	{ "synopsis.image.composition.pattern.fractal" : ["fractal texture", "fractal lens photography"]},
	],

 	"synopsis.image.composition.spatial" : [
 	{ "synopsis.image.composition.spatial.perspective" : ["perspective photography", "vanishing point photography"]},
	# needs better search terms?
	{ "synopsis.image.composition.spatial.orthographic" : ["orthographic photography", "orthographic photography"]},
	# needs better search terms?
	{ "synopsis.image.composition.spatial.isometric" : ["isometric photography"]},
	# needs better search terms?
	{ "synopsis.image.composition.spatial.open" : ["open composition photography",]},
	# needs better search terms?
	{ "synopsis.image.composition.spatial.closed" : ["spot texture", "spotted animal"]},
	{ "synopsis.image.composition.spatial.dense" : ["dense photography ", "maximalist photography"]},
	{ "synopsis.image.composition.spatial.sparse" : ["minimal photography"]},
	{ "synopsis.image.composition.spatial.horizon" : ["horizon", "vanishing point horizon photography"]},
	{ "synopsis.image.composition.spatial.verticality" : ["Verticality", "Verticality photography"]},
	{ "synopsis.image.composition.spatial.horitzontality" : ["horizontality photography -geography -geology"]},
	{ "synopsis.image.composition.spatial.diagonality" : ["diagonality composition photography"]},
	# remove images with the fucking grid over lay ahhhhhhhh
	{ "synopsis.image.composition.spatial.ruleofthirds" : ["rule of thirds composition photography"] },
	{ "synopsis.image.composition.spatial.negative " : ["negative space photography"] },
	{ "synopsis.image.composition.spatial.symmetric " : ["symmetrical photography"] },
 	],

	"synopsis.image.shot.angle" : [
	{ "synopsis.image.shot.angle.aerial" : ["aerial photography", "aerial shot"]},
	{ "synopsis.image.shot.angle.high" : ["high angle shot", "high angle shot film"]},
	{ "synopsis.image.shot.angle.eyelevel" : ["eye level shot", "eye level shot camera angle"]},
	{ "synopsis.image.shot.angle.low" : ["low angle shot", "low angle shot cinematography"]},
	{ "synopsis.image.shot.angle.tilted" : ["tilted shot", "dutch angle shot", "oblique angle shot"]},
	],

	"synopsis.image.shot.type" : [
	{ "synopsis.image.shot.type.establishing" : ["establishing shot", "establishing shot cinematography"]},
	{ "synopsis.image.shot.type.portrait" : ["portrait shot", "two shot cinematography"]},
	{ "synopsis.image.shot.type.twoshot" : ["two shot", "eye level shot camera angle"]},
	{ "synopsis.image.shot.type.master" : ["the master shot cinematography", "the master shot"]},
	{ "synopsis.image.shot.type.overtheshoulder" : ["over the shoulder shot", "over the shoulder shot cinematography"]},
	],

	"synopsis.image.shot.framing" : [
	{ "synopsis.image.shot.framing.extremecloseup" : ["extreme close up shot", "extreme close up shot cinematography"]},
	{ "synopsis.image.shot.framing.closeup" : ["close up shot", "close up shot cinematography"]},
	{ "synopsis.image.shot.framing.medium" : ["medium shot", "medium shot cinematography"]},
	{ "synopsis.image.shot.framing.long" : ["long shot", "long shot cinematography"]},
	{ "synopsis.image.shot.framing.extemelong" : ["extreme long shot", "extreme long shot cinematography"]},
	],

	"synopsis.image.shot.focus" : [
	{ "synopsis.image.shot.focus.deep" : ["deep focus shot", "deep focus shot cinematography"]},
	{ "synopsis.image.shot.focus.shallow" : ["shallow focus shot", "shallow focus shot cinematography"]},
	{ "synopsis.image.shot.focus.out" : ["out of focus shot"]},
	],

	"synopsis.image.shot.lighting" : [
	{ "synopsis.image.shot.lighting.soft" : ["soft lighting cinematography", "soft lighting"]},
	{ "synopsis.image.shot.lighting.hard" : ["hard lighting cinematography", "hard lighting"]},
	{ "synopsis.image.shot.lighting.lowkey" : ["low key lighting", "low key lighting cinematography"]},
	{ "synopsis.image.shot.lighting.highkey" : ["high key lighting", "high key lighting cinematography"]},
	{ "synopsis.image.shot.lighting.silhouette" : ["silhouette lighting", "silhouette lighting cinematography"]},
	],

	"synopsis.image.shot.subject" : [
	{ "synopsis.image.shot.subject.person" : ["portraits of people"]},
	{ "synopsis.image.shot.subject.people" : ["crowd of people", "people -lineart -clipart -animation", "people close together"]},
	# I cant figure out a better way to get diverse results :( - this feels gross - help me.
	# maybe https://www.ibm.com/blogs/research/2019/01/diversity-in-faces/ ? 
	{ "synopsis.image.shot.subject.face" : ["male face", "female face", "african american face", "asian face", "old face"]},
	# faces, body, bodies, limb, limbs might be too specific with the plurals? Maybe make one category?
	{ "synopsis.image.shot.subject.faces" : ["faces close together"]},
	{ "synopsis.image.shot.subject.body" : ["human figure photography", ]},
	{ "synopsis.image.shot.subject.bodies" : ["human figures photography"]},
	{ "synopsis.image.shot.subject.limb" : ["limb body photography", "limb figure photography"]},
	{ "synopsis.image.shot.subject.limbs" : ["limbs bodies photography" "limb figures photography"]},
	{ "synopsis.image.shot.subject.animal" : ["wildlife photography"]},
	{ "synopsis.image.shot.subject.object" : ["object photography", "still life photography"]},
	{ "synopsis.image.shot.subject.text" : ["typographic design", "movie title design"]},
	{ "synopsis.image.shot.subject.location" : ["location photography", "establishing shot"]},
	],

	"synopsis.image.shot.timeofday" : [
	{ "synopsis.image.shot.timeofday.twilight" : ["twilight time of day", "dusk", "sunset", "sunrise"]},
	{ "synopsis.image.shot.timeofday.day" : ["midday photography"]},
	{ "synopsis.image.shot.timeofday.night" : ["night photography"]},
	],

	"synopsis.image.shot.weather" : [
	{ "synopsis.image.shot.weather.sun" : ["Sun"]},
	{ "synopsis.image.shot.weather.clouds" : ["Clouds"]},
	{ "synopsis.image.shot.weather.rain" : ["Rain"]},
	{ "synopsis.image.shot.weather.fog" : ["Fog"]},
	{ "synopsis.image.shot.weather.snow" : ["Snow"]},
	{ "synopsis.image.shot.weather.lighting" : ["Lighting"]},
	{ "synopsis.image.shot.weather.hail" : ["Hail"]},
	{ "synopsis.image.shot.weather.fire" : ["Fire"]},
	],

	"synopsis.image.shot.location" : [
	{"synopsis.image.shot.location.interior" : ["Indoors", "Interior", "inside"]},
	{"synopsis.image.shot.location.exterior" : ["Outdoors", "Exterior", "outside"]},
	{"synopsis.image.shot.location.structure" : ["Structure", "man made"]},
	{"synopsis.image.shot.location.nature" : ["Nature", ""]},
	{"synopsis.image.shot.location.house" : ["House"]},
	{"synopsis.image.shot.location.apartment" : ["Apartment"]},
	{"synopsis.image.shot.location.mansion" : ["Mansion"]},
	{"synopsis.image.shot.location.building" : ["Building"]},
	{"synopsis.image.shot.location.room" : ["Room"]},
	{"synopsis.image.shot.location.hallway" : ["Hallway"]},
	{"synopsis.image.shot.location.livingroom" : ["Living Room"]},
	{"synopsis.image.shot.location.diningroom" : ["Dining Room"]},
	{"synopsis.image.shot.location.kitchen" : ["Kitchen"]},
	{"synopsis.image.shot.location.bedroom" : ["Bedroom"]},
	{"synopsis.image.shot.location.bathroom" : ["Bathroom"]},
	{"synopsis.image.shot.location.closet" : ["Closet"]},
	{"synopsis.image.shot.location.garage" : ["Garage"]},
	{"synopsis.image.shot.location.office" : ["Office"]},
	{"synopsis.image.shot.location.factory" : ["Factory"]},
	{"synopsis.image.shot.location.restaurant" : ["Restaurant"]},
	{"synopsis.image.shot.location.cafe" : ["Cafe"]},
	{"synopsis.image.shot.location.cafeteria" : ["Cafeteria"]},
	{"synopsis.image.shot.location.bar" : ["Bar"]},
	{"synopsis.image.shot.location.danceclub" : ["Dance Club"]},
	{"synopsis.image.shot.location.concerthall" : ["Concert Hall"]},
	{"synopsis.image.shot.location.houseofworship" : ["House Of Worship"]},
	{"synopsis.image.shot.location.store" : ["Store"]},
	{"synopsis.image.shot.location.city" : ["City"]},
	{"synopsis.image.shot.location.suburb" : ["Suburb"]},
	{"synopsis.image.shot.location.village" : ["Village"]},
	{"synopsis.image.shot.location.park" : ["Park"]},
	{"synopsis.image.shot.location.bridge" : ["Bridge"]},
	{"synopsis.image.shot.location.tunnel" : ["Tunnel"]},
	{"synopsis.image.shot.location.port" : ["Port"]},
	{"synopsis.image.shot.location.station" : ["Station"]},
	{"synopsis.image.shot.location.parkinglot" : ["Parking Lot"]},
	{"synopsis.image.shot.location.airport" : ["Airport"]},
	{"synopsis.image.shot.location.playground" : ["Playground"]},
	{"synopsis.image.shot.location.sidewalk" : ["Sidewalk"]},
	{"synopsis.image.shot.location.street" : ["Street"]},
	{"synopsis.image.shot.location.car" : ["Car"]},
	{"synopsis.image.shot.location.bus" : ["Bus"]},
	{"synopsis.image.shot.location.truck" : ["Truck"]},
	{"synopsis.image.shot.location.train" : ["Train"]},
	{"synopsis.image.shot.location.boat" : ["Boat"]},
	{"synopsis.image.shot.location.airplane" : ["Airplane"]},
	{"synopsis.image.shot.location.spaceship" : ["Spaceship"]},
	{"synopsis.image.shot.location.cockpit" : ["Cockpit"]},
	{"synopsis.image.shot.location.desert" : ["Desert"]},
	{"synopsis.image.shot.location.plains" : ["Plains"]},
	{"synopsis.image.shot.location.marsh" : ["Marsh"]},
	{"synopsis.image.shot.location.swamp" : ["Swamp"]},
	{"synopsis.image.shot.location.hillside" : ["Hillside"]},
	{"synopsis.image.shot.location.forest" : ["Forest"]},
	{"synopsis.image.shot.location.mountain" : ["Mountain"]},
	{"synopsis.image.shot.location.tundra" : ["Tundra"]},
	{"synopsis.image.shot.location.river" : ["River"]},
	{"synopsis.image.shot.location.lake" : ["Lake"]},
	{"synopsis.image.shot.location.ocean" : ["Ocean"]},
	{"synopsis.image.shot.location.canyon" : ["Canyon"]},
	{"synopsis.image.shot.location.glacier" : ["Glacier"]},
	{"synopsis.image.shot.location.space" : ["Space"]},
	],

"synopsis.image.sentiment" : [
	{ "synopsis.image.sentiment.fear" : ["Fear photography"]},
	{ "synopsis.image.sentiment.anger" : ["Anger photography"]},
	{ "synopsis.image.sentiment.sadness" : ["Sadness photography"]},
	{ "synopsis.image.sentiment.joy" : ["Joy photography"]},
	{ "synopsis.image.sentiment.disgust" : ["Disgust photography"]},
	{ "synopsis.image.sentiment.surprise" : ["Surprise photography"]},
	{ "synopsis.image.sentiment.trust" : ["Trust photography"]},
	{ "synopsis.image.sentiment.anticipation" : ["Anticipation photography"]},
	],

 }

#print categories_and_classes

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
			arguments = { "keywords" : searchterms, "limit" : 100, "print_urls" : False, "output_directory" : "Data/download/"+category_key, "image_directory" : concept_key,  "size" : "medium", "format" : "jpg" , "no_numbering" : True }
			#arguments = { "keywords" : searchterms, "limit" : 100, "print_urls" : False, "output_directory" : "Data/download/"+category_key, "image_directory" : concept_key,  "size" : "medium", "save_source" : concept_key + "sources", "format" : "jpg" }
			paths = response.download(arguments)
			print(paths)

#arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
#paths = response.download(arguments)   #passing the arguments to the function
#print(paths)   #printing absolute paths of the downloaded images