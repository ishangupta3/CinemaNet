## Labels Obverview 

TL/DR:

* Labels are currently a work in progress (WIP) for 1.0.
* Labels can be thought of as tags / attributes, not as a single classification with the Synopsis model. ie: A file may have multiple classifications associated with it assuming high enough probability. See Coco Attributes for an example of an attribute / multiclass labelling model.
* Labels use a reverse dns nomenclature from category to specific concepts and sub concepts. For example: 

A single frame might be tagged with:
* `color.saturation.neutral`
* `color.theory.analagous`
* `compositon.texture.smooth`
* `shot.framing.closeup`
* `shot.subject.person`
* `shot.subject.person.face`
* `shot.location.indoor`
* `shot.location.room`
* `shot.location.room.livingroom`

This allows us to build a pseudo knowledge graph and not pollute name spaces of labels. Currently labels are broken up into a few main categories their individual named concepts.


### Labels proposal for 1.0

Note that inorder to label a large data set, we train image classifiers (not multi label) on sub sets of concepts the proposed concepts that are mutually exclusive conceptually.

* `Color`
* `Composition`
* `Shot`

## Color:

> Color psychology and color theory

#### color.saturation
> How do we describe the overall saturation of the image
* `color.saturation.desaturated`
* `color.saturation.muted`
* `color.saturation.neutral`
* `color.saturation.pastel`
* `color.saturation.saturated`

#### color.theory 
> How do we describe the color relationship in the image
* `color.theory.na` (not applicable)
* `color.theory.analagous`
* `color.theory.complementary`
* `color.theory.monochromatic`

#### color.tones 
> How do we describe the color temperature and tone in the image
* `color.tones.na` (not applicable)
* `color.tones.blackwhite`
* `color.tones.cool`
* `color.tones.warm`

### color.key
> Does the image contain a luma or chroma key?
* `color.key.na` (not applicable)
* `color.key.luma`
* `color.key.green`
* `color.key.blue`

#### color.dominant
> How do we describe the human readable dominant colors - using most commonly used color names
* `color.dominant.na` (not applicable)
* `color.dominant.white`
* `color.dominant.grey`
* `color.dominant.black`
* `color.dominant.red`
* `color.dominant.orange`
* `color.dominant.yellow`
* `color.dominant.lime`
* `color.dominant.green`
* `color.dominant.cyan`
* `color.dominant.blue`
* `color.dominant.purple`
* `color.dominant.magenta`
* `color.dominant.brown`

## Composition: (WIP)

>Taken from Gestalt Theory and graphic design / layout systems thinking

#### composition.pattern (WIP)
> Does the image strogly consist of a pattern, and if so, what type of pattern?
* `composition.pattern.na` (not applicable)
* `composition.pattern.fractal`
* `composition.pattern.reflect`
* `composition.pattern.spiral`
* `composition.pattern.spot`
* `composition.pattern.stripe`
* `composition.pattern.tile`

#### composition.spatial (WIP)
> How can we descibe the spatial layout and composition of the image?
* `composition.spatial.perspective`
* `composition.spatial.orthographic`
* `composition.spatial.isometric`
* `composition.spatial.open`
* `composition.spatial.closed`
* `composition.spatial.dense`
* `composition.spatial.sparse`
* `composition.spatial.horizon`
* `composition.spatial.verticality`
* `composition.spatial.horitzontality`
* `composition.spatial.diagonality`
* `composition.spatial.ruleofthirds`
* `composition.spatial.negativespace `
* `composition.spatial.symmetric`
* `composition.spatial.centered `
* `composition.spatial.offcenter`

#### composition.texture (WIP)
> How can we describe the image in terms of visual texture
* `composition.texture.natural`
* `composition.texture.synthetic`
* `composition.texture.harmonious`
* `composition.texture.dissonant`
* `composition.texture.smooth`
* `composition.texture.rough`
* `composition.texture.cracked`
* `composition.texture.patterned`

### Shot:

>Categories and concepts dervied from cinematography and photography concepts

### shot.angle
>How do we describe the image in terms of camera orientation and placement with respect to height?
* `shot.angle.na` (not applicable)
* `shot.angle.aerial`
* `shot.angle.birdseye`
* `shot.angle.high`
* `shot.angle.eyelevel`
* `shot.angle.low`

### shot.level
> How do we descrive the image in terms of camera orientation with respect to rotation along the direction of the lens?
* `shot.level.na` (not applicable)
* `shot.level.level`
* `shot.level.tilted`

### shot.type
>How do we describe the image in terms of cinemographic shot type language?
* `shot.type.na` (not applicable)
* `shot.type.portrait`
* `shot.type.twoshot`
* `shot.type.master`
* `shot.type.overtheshoulder`

### shot.framimg
>How do we describe the image in terms of camera proximity to the subject (typically a person)
* `shot.framing.na` (not applicable)
* `shot.framing.extremecloseup`
* `shot.framing.closeup`
* `shot.framing.medium`
* `shot.framing.long`
* `shot.framing.extremelong`

### shot.focus
>How do we descibe the image in terms of camera focus
* `shot.focus.na` (not applicable)
* `shot.focus.deep`
* `shot.focus.shallow`
* `shot.focus.out`

### shot.lighting (WIP)
>How do we describe the lighting of the subject in the image
* `shot.lighting.na` (not applicable)
* `shot.lighting.soft`
* `shot.lighting.hard`
* `shot.lighting.lowkey`
* `shot.lighting.highkey`
* `shot.lighting.silhouette`

### shot.subject
>What is the subject of the image, if any?
* `shot.subject.na` (not applicable)
* `shot.subject.animal`
* `shot.subject.object`
* `shot.subject.text`
* `shot.subject.location`
* `shot.subject.person`

>If the subject of the image is a person, are we focusing on a particular location on the body?
* `shot.subject.person.face`
* `shot.subject.person.arm`
* `shot.subject.person.hand`

### shot.timeofday
>What is the time of day in the image, if any?
* `shot.timeofday.na` (not applicable)
* `shot.timeofday.twilight (dawn or dusk)`
* `shot.timeofday.day`
* `shot.timeofday.night`

### shot.weather (WIP)
>What is the weather in the image, if any?
* `shot.weather.na` (not applicable)
* `shot.weather.sunny`
* `shot.weather.cloudy`
* `shot.weather.raining`
* `shot.weather.snowing`

### shot.location (WIP)
>How do we describe the location of the subject / camera in the image, if any? Borrows heavily from ideas in Places 365
* `shot.location.na` (not applicable)
* `shot.location.interior` (indoors / inside)
* `shot.location.exterior` (outdoors / outside)

>Specific nature (exterior) categories if we can identify them
* `shot.location.exterior.beach`
* `shot.location.exterior.cave` (cave entrance)
* `shot.location.exterior.desert`
* `shot.location.exterior.plains`
* `shot.location.exterior.wetlands`
* `shot.location.exterior.hills`
* `shot.location.exterior.forest`
* `shot.location.exterior.mountain`
* `shot.location.exterior.polar` (artic, antartic)
* `shot.location.exterior.river`
* `shot.location.exterior.lake`
* `shot.location.exterior.ocean`
* `shot.location.exterior.canyon`
* `shot.location.exterior.glacier`
* `shot.location.exterior.space`
* `shot.location.exterior.sky`

>Specific township (exterior) categories if we can identify them
* `shot.location.exterior.city`
* `shot.location.exterior.town`
* `shot.location.exterior.suburb` 
* `shot.location.exterior.park`
* `shot.location.exterior.playground`
* `shot.location.exterior.sidewalk`
* `shot.location.exterior.street` 

>Specific building (exterior) categories if we can identify them
* `shot.location.exterior.house`
* `shot.location.exterior.mansion`
* `shot.location.exterior.apartment`
* `shot.location.exterior.castle`
* `shot.location.exterior.skyscraper`
* `shot.location.exterior.palace`
* `shot.location.exterior.office`
* `shot.location.exterior.factory`
* `shot.location.exterior.farm`
* `shot.location.exterior.restaurant`
* `shot.location.exterior.bar` (or pub)
* `shot.location.exterior.cafe`
* `shot.location.exterior.chruch`
* `shot.location.exterior.mosque`
* `shot.location.exterior.synagogue`
* `shot.location.exterior.temple`
* `shot.location.exterior.cathedral`
* `shot.location.exterior.monastery`
* `shot.location.exterior.stadium`
* `shot.location.exterior.theater` 
* `shot.location.exterior.garage`
* `shot.location.exterior.store`
* `shot.location.exterior.mall`
* `shot.location.exterior.port`
* `shot.location.exterior.pier`
* `shot.location.exterior.warehouse`
* `shot.location.exterior.ruins`
* `shot.location.exterior.concerthall`
* `shot.location.exterior.nightclub`
* `shot.location.exterior.airport`
* `shot.location.exterior.station.train`
* `shot.location.exterior.station.gas`
* `shot.location.exterior.station.bus`
* `shot.location.exterior.station.subway`
* `shot.location.exterior.hospital`
* `shot.location.exterior.school`
* `shot.location.exterior.library`
* `shot.location.exterior.parkinglot`
* `shot.location.exterior.bridge`
* `shot.location.exterior.tunnel` (entrance)


>Specific vehicle (exterior) categories if we can identify them
* `shot.location.exterior.car`
* `shot.location.exterior.bus`
* `shot.location.exterior.motorcycle`
* `shot.location.exterior.bicycle`
* `shot.location.exterior.truck`
* `shot.location.exterior.train`
* `shot.location.exterior.boat`
* `shot.location.exterior.airplane`
* `shot.location.exterior.spacecraft`


>Specific room (interior) categories if we can identify them
* `shot.location.interior.cave`
* `shot.location.interior.lobby`
* `shot.location.interior.foyer`
* `shot.location.interior.hallway`
* `shot.location.interior.livingroom`
* `shot.location.interior.diningroom`
* `shot.location.interior.kitchen`
* `shot.location.interior.closet`
* `shot.location.interior.bedroom`
* `shot.location.interior.bathroom`
* `shot.location.interior.closet`
* `shot.location.interior.garage`
* `shot.location.interior.auditorium`
* `shot.location.interior.gym`
* `shot.location.interior.emergencyroom`
* `shot.location.interior.study`
* `shot.location.interior.stairwell`
* `shot.location.interior.elevator`
* `shot.location.interior.garage`
* `shot.location.interior.factory` (factory line, factory floor)
* `shot.location.interior.warehouse` 
* `shot.location.interior.dungeon` 
* `shot.location.interior.throneroom` 
* `shot.location.interior.classroom`
* `shot.location.interior.cafeteria`
* `shot.location.interior.office`
* `shot.location.interior.openoffice`
* `shot.location.interior.conferenceroom`
* `shot.location.interior.barn`
* `shot.location.interior.restaurant`
* `shot.location.interior.commercialkitchen`
* `shot.location.interior.bar`
* `shot.location.interior.cafe`
* `shot.location.interior.arena`
* `shot.location.interior.stage`
* `shot.location.interior.dancefloor`
* `shot.location.interior.airport` (terminal)
* `shot.location.interior.station.train` (terminal)
* `shot.location.interior.station.bus` (terminal)
* `shot.location.interior.station.subway` (subway platform, subway turnstyle, subway car)
* `shot.location.interior.store`
* `shot.location.interior.aisle` (store)
* `shot.location.interior.checkout` (store)
* `shot.location.interior.mall`
* `shot.location.interior.nave`
* `shot.location.interior.pulpit`
* `shot.location.interior.prayerhall`
* `shot.location.interior.synegogue`
* `shot.location.interior.meditation`
* `shot.location.interior.grandhall`
* `shot.location.interior.crypt`
* `shot.location.interior.cloister`

>Specific vehicle (interior) if we can identify them
* `shot.location.interior.car`
* `shot.location.interior.bus`
* `shot.location.interior.truck`
* `shot.location.interior.train`
* `shot.location.interior.subway` (subway car)
* `shot.location.interior.subway` (subway car)
* `shot.location.interior.boat` 
* `shot.location.interior.airplane` (cockpit, cabin)
* `shot.location.interior.spacecraft` (cockpit, cabin)

