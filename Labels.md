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
* `shot.location.interior` (indoors, inside)
* `shot.location.exterior` (outdoors / outside)
* `shot.location.nature` (ie, not a human made construction)
* `shot.location.building` (any type of building)
* `shot.location.room` (any type of room)
* `shot.location.township` (any collection of buildings / community / city / village etc)
* `shot.location.vehicle` (inside or outside of a vehicle)

>Specific nature categories if we can identify them
* `shot.location.nature.cave`
* `shot.location.nature.desert`
* `shot.location.nature.plains`
* `shot.location.nature.marsh`
* `shot.location.nature.swamp`
* `shot.location.nature.hillside`
* `shot.location.nature.forest`
* `shot.location.nature.mountain`
* `shot.location.nature.tundra`
* `shot.location.nature.river`
* `shot.location.nature.lake`
* `shot.location.nature.ocean`
* `shot.location.nature.canyon`
* `shot.location.nature.glacier`
* `shot.location.nature.space`
* `shot.location.nature.sky`

>Specific building categories if we can identify them
* `shot.location.building.house`
* `shot.location.building.mansion`
* `shot.location.building.apartment`
* `shot.location.building.castle`
* `shot.location.building.office`
* `shot.location.building.factory`
* `shot.location.building.farm`
* `shot.location.building.restaurant`
* `shot.location.building.bar (pub)`
* `shot.location.building.cafe`
* `shot.location.building.chruch`
* `shot.location.building.mosque`
* `shot.location.building.synagogue`
* `shot.location.building.temple`
* `shot.location.building.cathedral`
* `shot.location.building.monastery`
* `shot.location.building.stadium`
* `shot.location.building.theater (hall)`
* `shot.location.building.garage`
* `shot.location.building.store`
* `shot.location.building.mall`
* `shot.location.building.port`
* `shot.location.building.pier`
* `shot.location.building.warehouse`
* `shot.location.building.ruins`
* `shot.location.building.concerthall`
* `shot.location.building.nightclub`
* `shot.location.building.buildng.airport`
* `shot.location.building.station.train`
* `shot.location.building.station.gas`
* `shot.location.building.station.bus`
* `shot.location.building.station.subway`
* `shot.location.building.hospital`
* `shot.location.building.school`
* `shot.location.building.parkinglot`
* `shot.location.building.bridge`
* `shot.location.building.tunnel`

>Specific room categories if we can identify them
* `shot.location.room.hallway`
* `shot.location.room.living`
* `shot.location.room.dining`
* `shot.location.room.kitchen`
* `shot.location.room.bed`
* `shot.location.room.bath`
* `shot.location.room.closet`
* `shot.location.room.garage`
* `shot.location.room.auditorium`
* `shot.location.room.gym`
* `shot.location.room.emergency`
* `shot.location.room.stairwell`

>Specific township categories if we can identify them
* `shot.location.township.city`
* `shot.location.township.town`
* `shot.location.township.suburb` 
* `shot.location.township.park`
* `shot.location.township.playground`
* `shot.location.township.sidewalk`
* `shot.location.township.street` 

>Specific vehicle categories if we can identify them
* `shot.location.vehicle.car`
* `shot.location.vehicle.bus`
* `shot.location.vehicle.truck`
* `shot.location.vehicle.train`
* `shot.location.vehicle.boat`
* `shot.location.vehicle.airplane`
* `shot.location.vehicle.spaceship`
