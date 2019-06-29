from google_images_download import google_images_download   #importing the library
from multiprocessing import Pool
import os

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
	"color_saturation" : [
	{ "color_saturation_desaturated" : ["Desaturated photography", "Desaturated colors photography", "Desaturated tones photography"]},
	{ "color_saturation_muted" : ["muted photography", "muted colors photography", "muted tones photography"]},
	{ "color_saturation_neutral" : ["neutral photography", "neutral colors photography", "neutral tones photography"]},
	{ "color_saturation_pastel" : ["Pastel photography", "Pastel colors photography", "Pastel tones photography"]},
	{ "color_saturation_saturated" : ["Saturated photography", "Saturated colors photography"]},
	],

	# How do the colors in the image relate to one another?
	# do we need a `none of the above`?
	"color_theory" : [
	# contains NA when training
	{ "color_theory_analagous" : ["Analagous photography", "Analagous color photography"]},
	{ "color_theory_complementary" : ["complementary photography", "Complementary color photography"]},
	{ "color_theory_monochromatic" : ["Monochromatic photography", "Monochromatic color photography", ]},
	],

	# Overall color tone of the image
	"color_tones" : [
	# contains NA when training
	{ "color_tones_blackwhite" :  ["Black and White photography", "B&W photography"] },
	{ "color_tones_cool" : ["Cool Tones photography", "Cool colors photography"]},
	{ "color_tones_warm" : ["Warm Tones  photography", "Warm colors  photography"]},
	],

	# Is the image useful for keying?
	"color_key" : [
	# contains NA when training
	{ "color_key_luma" : ["luma key"]},
	{ "color_key_green" : ["green screen", "chroma key green"]},
	{ "color_key_blue" : ["blue screen", "chroma key blue"]},
	],

	# color.dominant is created manually

	"composition_pattern" : [
	# contains NA when training
	{ "composition_pattern_tile" : ["tiled texture", "tiled photography"]},
	{ "composition_pattern_spiral" : ["spiral texture", "spiral nature photography"]},
	# needs better search terms?
	{ "composition_pattern_reflect" : ["glide reflection pattern"]},
	{ "composition_pattern_stripe" : ["striped pattern", "stripes photography"]},
	{ "composition_pattern_spot" : ["spot texture", "spotted animal"]},
	{ "composition_pattern_fractal" : ["fractal texture", "fractal lens photography"]},
	],

	"composition_spatial" : [
 	{ "composition_spatial_perspective" : ["perspective photography", "vanishing point photography"]},
	# needs better search terms?
	{ "composition_spatial_orthographic" : ["orthographic photography", "orthographic photography"]},
	# needs better search terms?
	{ "composition_spatial_isometric" : ["isometric photography"]},
	# needs better search terms?
	{ "composition_spatial_open" : ["open composition photography",]},
	# needs better search terms?
	{ "composition_spatial_closed" : ["spot texture", "spotted animal"]},
	{ "composition_spatial_dense" : ["dense photography ", "maximalist photography"]},
	{ "composition_spatial_sparse" : ["minimal photography"]},
	{ "composition_spatial_horizon" : ["horizon", "vanishing point horizon photography"]},
	{ "composition_spatial_verticality" : ["Verticality", "Verticality photography"]},
	{ "composition_spatial_horitzontality" : ["horizontality photography -geography -geology"]},
	{ "composition_spatial_diagonality" : ["diagonality composition photography"]},
	# remove images with the fucking grid over lay ahhhhhhhh
	{ "composition_spatial_ruleofthirds" : ["rule of thirds composition photography"] },
	{ "composition_spatial_negative " : ["negative space photography"] },
	{ "composition_spatial_symmetric " : ["symmetrical photography"] },

	# sub-category
	{ "composition_spatial_centered" : ["centered composition", "centered photography"] },
    { "composition_spatial_offcentered" : ["off centered photography", "off centered composition"] },

 	],


	# train natural vs synthetic in one classifier
	"composition_texture" : [
	{ "composition_texture_natural" : ["natural texture", "organic texture"]},
	{ "composition_texture_synthetic" : ["synthetic texture", "technical texture"]},

	# train harmonious vs dissonant in one classifier
	{ "composition_texture_harmonious" : ["harmonious texture", "harmonious photography composition"]},
	{ "composition_texture_dissonant" : ["dissonant texture", "chaotic texture", "disordered photography"]},
	
	#train smooth vs rough in one classifier
	{ "composition_texture_smooth" : ["smooth texture", "smooth photography"]},
	{ "composition_texture_rough" : ["rough texture", "rough texture photography"]},

	# train cracked vs patterned (continuous?)	
	{ "composition_texture_cracked" : ["rough texture", "rough photography"]},
	{ "composition_texture_patterned" : ["pattern texture", "pattern photography"]},
	],	
 	
 	#is the camera is angled up or down?
	"shot_angle" : [
	# contains NA when training
	{ "shot_angle_aerial" : ["aerial photography", "aerial shot"]},
	{ "shot_angle_high" : ["high angle shot", "high angle shot film"]},
	{ "shot_angle_eyelevel" : ["eye level shot", "eye level shot camera angle"]},
	{ "shot_angle_low" : ["low angle shot", "low angle shot cinematography"]},
	],
	
	# is the camera rotated about its 'z axis'? (rotated about the lens)
	"shot_level" : [
	# contains NA when training
	{ "shot_level_level" : ["level shot"]},
	{ "shot_level_tilted" : ["tilted shot", "dutch angle shot", "oblique angle shot"]},
	],

	# 
	"shot_type" : [
	# contains NA when training
	{ "shot_type_portrait" : ["portrait shot", "two shot cinematography"]},
	{ "shot_type_twoshot" : ["two shot", "eye level shot camera angle"]},
	{ "shot_type_master" : ["the master shot cinematography", "the master shot", "band photo"]},
	# Trained as a seperate concept - but still a type (ie, can have a over the shoulder two shot)
	{ "shot)type_overtheshoulder" : ["over the shoulder shot", "over the shoulder shot cinematography"]},
	],

	# how far are we from the shot subject?
	"shot_framing" : [
	{ "shot_framing_extremecloseup" : ["extreme close up shot", "extreme close up shot cinematography"]},
	{ "shot_framing_closeup" : ["close up shot", "close up shot cinematography"]},
	{ "shot_framing_medium" : ["medium shot", "medium shot cinematography"]},
	{ "shot_framing_long" : ["long shot", "long shot cinematography"]},
	{ "shot_framing_extemelong" : ["extreme long shot", "extreme long shot cinematography"]},
	],

	# is the image completely, partially or not in focus?
	"shot_focus" : [
	# contains NA when training
	{ "shot_focus_deep" : ["deep focus shot", "deep focus shot cinematography"]},
	{ "shot_focus_shallow" : ["shallow focus shot", "shallow focus shot cinematography"]},
	{ "shot_focus_out" : ["out of focus", "out of focus shot"]},
	],

	# describe the lighting environment 
	"shot_lighting" : [
	# contains NA when training
	{ "shot_lighting_soft" : ["soft lighting cinematography", "soft lighting"]},
	{ "shot_lighting_hard" : ["hard lighting cinematography", "hard lighting"]},
	{ "shot_lighting_lowkey" : ["low key lighting", "low key lighting cinematography"]},
	{ "shot_lighting_highkey" : ["high key lighting", "high key lighting cinematography"]},
	{ "shot_lighting_silhouette" : ["silhouette lighting", "silhouette lighting cinematography"]},
	],

	# what is the - generally speaking - subject of the shot, if any
	"shot_subject" : [
	# contains NA when training
	{ "shot_subject_person" : ["diverse portraits photography", "portraits of people", "people -lineart -clipart -animation"]},
	{ "shot_subject_animal" : ["wildlife photography"]},
	{ "shot_subject_object" : ["object photography", "still life photography"]},
	{ "shot_subject_text" : ["typographic design", "movie title design"]},
	{ "shot_subject_location" : ["location photography", "establishing shot"]},
	],

	# I cant figure out a better way to get diverse results :( - this feels gross - help me.
	# maybe https://www.ibm.com/blogs/research/2019/01/diversity-in-faces/ ? 
	# faces, body, bodies, limb, limbs might be too specific with the plurals? Maybe make one category?
	"shot_subject_person" : [
	{ "shot_subject_person_face" : ["male face", "female face", "african american face", "asian face", "old face", "diverse faces photography -collage"]},
	{ "shot_subject_person_body" : ["diverse human figure photography", "diverse body shapes portraits"]},
	{ "shot_subject_person_arms" : ["arms photography", "arms outreached photography", "arms crossed photography"]},
	{ "shot_subject_person_hands" : ["hands photography", "fist photography", "holding hands photography"]},
	],

	# self explanatory
	"shot_timeofday" : [
	# contains NA when training
	{ "shot_timeofday_twilight" : ["twilight time of day", "dusk", "sunset", "sunrise"]},
	{ "shot_timeofday_day" : ["midday photography"]},
	{ "shot_timeofday_night" : ["night photography"]},
	],

	# self explanatory
	"shot_weather" : [
	# contains NA when training
	{ "shot_weather_sunny" : ["Sunny weather"]},
	{ "shot_weather_cloudy" : ["Cloudy weather"]},
	{ "shot_weather_raining" : ["Rainy weather"]},
	{ "shot_weather_snowing" : ["Snowy weather"]},
	# foggy?
	# stormy?
	],

	# self explanatory
	"shot_location" : [
	# contains NA when training

	# Trained as a seperate concepts
	{"shot_location_interior" : ["Indoors", "Interior", "inside"]},
	{"shot_location_exterior" : ["Outdoors", "Exterior", "outside"]},


	# Trained as a seperate set of concept 
	{"shot_location_nature" : ["Nature"]},
	# all the building subcategories are also used
	{"shot_location_building" : ["building", "structure"]},	
	# all the 'room' subcategories are also used
	{"shot_location_room" : ["Room"]},
	# all the township sub categories are also used
	{"shot_location_township" : ["modern township -game"]},
	# all the vehicle sub categories are also used
	{"shot_location_vehicle" : ["vehicle -cartoon -toy"]},

	# all sub categories trained as a sepearate set of concepts, with their own internal 'na' categories

	# specific nature categories
	{"shot_location_nature_beach" : ["Beach"]},
	{"shot_location_nature_cave" : ["Caves"]},
	{"shot_location_nature_desert" : ["Desert"]},
	{"shot_location_nature_plains" : ["Plains"]},
	{"shot_location_nature_marsh" : ["Marsh"]},
	{"shot_location_nature_swamp" : ["Swamp"]},
	{"shot_location_nature_hillside" : ["Hillside"]},
	{"shot_location_nature_forest" : ["Forest"]},
	{"shot_location_nature_mountain" : ["Mountains"]},
	{"shot_location_nature_tundra" : ["Tundra"]},
	{"shot_location_nature_river" : ["River"]},
	{"shot_location_nature_lake" : ["Lake"]},
	{"shot_location_nature_ocean" : ["Ocean"]},
	{"shot_location_nature_canyon" : ["Canyon"]},
	{"shot_location_nature_glacier" : ["Glacier"]},
	{"shot_location_nature_sky" : ["Sky"]},
	# {"shot_location_nature_space" : ["Space"]},

	# specific building categories
	{"shot_location_building_house" : ["House"]},
	{"shot_location_building_mansion" : ["Mansion"]},
	{"shot_location_building_apartment" : ["Apartment"]},
	{"shot_location_building_castle" : ["Castle"]},
	{"shot_location_building_office" : ["Office"]},
	{"shot_location_building_farm" : ["Farm"]},
	{"shot_location_building_factory" : ["Factory"]},
	{"shot_location_building_restaurant" : ["Restaurant"]},
	{"shot_location_building_bar" : ["Bar", "pub"]},
	{"shot_location_building_cafe" : ["Cafe"]},
	{"shot_location_building_church" : ["Church"]},
	{"shot_location_building_mosque" : ["Mosque" ]},
	{"shot_location_building_temple" : ["Temple"]},
	{"shot_location_building_synagogue" : ["Synagogue"]},
	{"shot_location_building_cathedral" : ["Cathedral"]},
	{"shot_location_building_monastery" : ["Monastery"]},
	{"shot_location_building_stadium" : ["stadium"]},
	{"shot_location_building_theater" : ["theater"]},
	{"shot_location_building_garage" : ["garage"]},
	{"shot_location_building_store" : ["Store"]},
	{"shot_location_building_mall" : ["Mall"]},
	{"shot_location_building_port" : ["Port", ]},
	{"shot_location_building_pier" : ["Pier"]},
	{"shot_location_building_warehouse" : ["Warehouse"]},
	{"shot_location_building_ruins" : ["Ruins", "modern ruins"]},
	{"shot_location_building_concerthall" : ["Concert Hall"]},
	{"shot_location_building_nightclub" : ["Night Club"]},
	{"shot_location_building_buildng.airport" : ["Airport"]},
	{"shot_location_building_station_train" : ["Train Station"]},
	{"shot_location_building_station_gas" : ["Gas Station"]},
	{"shot_location_building_station_bus" : ["Bus Station"]},
	{"shot_location_building_subway" : ["Subway Station", "Subway -sandwich -food"]},
	{"shot_location_building_hospital" : ["Hospital"]},	
	{"shot_location_building_school" : ["School"]},	
	{"shot_location_building_parkinglot" : ["Parking Lot"]},
	{"shot_location_building_bridge" : ["Bridge"]},
	{"shot_location_building_tunnel" : ["Tunnel"]},

	# specific room categories
	{"shot_location_room_hallway" : ["Hallway"]},
	{"shot_location_room_living" : ["Living Room"]},
	{"shot_location_room_dining" : ["Dining Room"]},
	{"shot_location_room_kitchen" : ["Kitchen"]},
	{"shot_location_room_bed" : ["Bedroom"]},
	{"shot_location_room_bath" : ["Bathroom"]},
	{"shot_location_room_closet" : ["Closet"]},
	{"shot_location_room_garage" : ["Garage"]},
	{"shot_location_room_auditorium" : ["Auditorium"]},
	{"shot_location_room_gym" : ["Gym"]},
	{"shot_location_room_emergency" : ["Emergency Room"]},
	{"shot_location_room_stairwell" : ["Stairwell"]},

	# specific township categories
	{"shot_location_township_city" : ["City"]},
	{"shot_location_township_town" : ["Town"]},
	{"shot_location_township_suburb" : ["Suburb"]},
	{"shot_location_township_park" : ["Park"]},
	{"shot_location_township_playground" : ["Playground"]},
	{"shot_location_township_sidewalk" : ["city sidewalk photography"]},
	{"shot_location_township_street" : ["Street"]},

	# specific vehicle categories
	{"shot_location_vehicle_car" : ["Car"]},
	{"shot_location_vehicle_bus" : ["Bus"]},
    {"shot_location_vehicle_truck" : ["Truck"]},
	{"shot_location_vehicle_motorcycle" : ["Motorcycle riding"]}, #riding removes all white images background images
	{"shot_location_vehicle_bicycle" : ["Bicycle riding"]}, #riding removes all white background images
	{"shot_location_vehicle_bus" : ["Bus"]},
	{"shot_location_vehicle_train" : ["Train"]},
	{"shot_location_vehicle_boat" : ["Boat"]},
	{"shot_location_vehicle_airplane" : ["Airplane"]},
	{"shot_location_vehicle_spaceship" : ["Spaceship"]},
	],


 }

#print categories_and_classes

def download_images(arguments):
			response = google_images_download.googleimagesdownload()   #class instantiation
			paths = response.download(arguments)
			print(paths)

allArguments = []

try:
    os.stat("Data/download/")
except:
    os.mkdir("Data/download/")   

for category_key in categories_and_concepts:
	# concepts is an array of dictionaries

	try:
	    os.stat("Data/download/" + category_key)
	except:
	    os.mkdir("Data/download/" + category_key)   

	print "Category: " + category_key
	category_concepts = categories_and_concepts[category_key] 
	for concept in category_concepts:
		for concept_key in concept:
			print "Concept: " + concept_key 
			searchterms = ", ".join(concept[concept_key])
			print "Search Terms: " + searchterms

			try:
			    os.stat("Data/download/" + catcategory_key + "/" + concept_keyegory_key)
			except:
			    os.mkdir("Data/download/" + category_key + "/" + concept_key)   

			response = google_images_download.googleimagesdownload()   #class instantiation
			arguments = { "chromedriver" : "/Users/vade/Documents/Repositories/Synopsis/CinemaNet/chromedriver", "keywords" : searchterms, "limit" : 300, "print_urls" : False, "output_directory" : "Data/download/"+category_key, "image_directory" : concept_key,  "size" : "medium", "format" : "jpg" , "no_numbering" : True }
			#arguments = { "keywords" : searchterms, "limit" : 100, "print_urls" : False, "output_directory" : "Data/download/"+category_key, "image_directory" : concept_key,  "size" : "medium", "save_source" : concept_key + "sources", "format" : "jpg" }
			allArguments.append(arguments)

# concurrent google image downloaders
pool = Pool(processes=10)
results = pool.map(download_images, allArguments)

print(results)
