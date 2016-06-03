# OpenPianosMap

## Overview

The goal of this project is to create an open source map of accessibles pianos (freely or not).
Data will be hosted on OpenStreetMap.

For the moment, the project is just a filter defined on [MapContrib](https://github.com/MapContrib/MapContrib) and there's no way to distinguish freely accessible pianos than piano bars (where pianos are only reserved for hired musicians).

The map is here :
http://www.cartes.xyz/t/e5c83c-Pianos_map

## Tags used

Current filter is:

```
node["musical_instrument"="piano"];
way["musical_instrument"="piano"];
node["amenity"="piano"];
node["musical_instrument:piano"="yes"]
way["musical_instrument:piano"="yes"]
```

## Tags stats

Here is a taginfo link to compare usage of:
  - musical_instrument=piano
  - amenity=piano
  - musical_instrument:piano=yes

https://taginfo.openstreetmap.org/compare/musical_instrument=piano/amenity=piano/musical_instrument:piano=yes/

## TODO

This are informations to add via OSM tags

### Add access info

For the moment, there's no way to distinguish a bar with a place with a piano freely accessible and a place with a piano, but only reserved for concert for example.
As the aim of the project is to quickly find on a map freely accessible pianos, it's an important point to decide.

What not using [access](http://wiki.openstreetmap.org/wiki/FR:Key:access) tag as it's used by the (toilets)[http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dtoilets] tag ?
For me its make sens to see:

  - *access=yes* explicitly public and open to whoever.
  - *access=permissive* while nominally private, no visible attempt is made to restrict access, and casual use appears to be tolerated by the owners.
  - *access=customers* while open to the public, the clear policy is to require a purchase prior to use. You may need a key or code to get in. Some people also use access=destination for this.

Of course, all that tags should only be used for nodes, not ways.

I'll make a proposal when it's more clear for me.
