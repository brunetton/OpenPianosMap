# OpenPianosMap

## Overview

The goal of this project is to create an open source map of accessibles pianos. Data will be hosted on OpenStreetMap

For the moment, the project is just a filter defined on [MapContrib](https://github.com/MapContrib/MapContrib).

The map is here :
http://www.cartes.xyz/t/e5c83c-Pianos_map

## Tags used

Current filter is:

```
node["musical_instrument"="piano"];
way["musical_instrument"="piano"];
node["amenity"="piano"];
node["musical_instrument:piano=yes"]
way["musical_instrument:piano=yes"]
```

## Tags stats

Here is a taginfo link to compare usage of:
  - musical_instrument=piano
  - amenity=piano
  - musical_instrument:piano=yes

https://taginfo.openstreetmap.org/compare/musical_instrument=piano/amenity=piano/musical_instrument:piano=yes/
