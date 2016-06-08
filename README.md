# OpenPianosMap

![](images/screenshot.png)

## Overview

The goal of this project is to create an open source map of accessibles pianos (freely or not).
Data will be hosted on OpenStreetMap.

For the moment, the project is "just" a filter defined on [MapContrib](https://github.com/MapContrib/MapContrib).

The map is here :
http://www.cartes.xyz/t/e5c83c-Pianos_map

## Tags used

  - for free access pianos (**green** on map):
    - nodes with `amenity=piano`
    - nodes with `musical_instrument=piano`
    - nodes with `musical_instrument:piano=yes`
    - with:
      - `access=yes`
      - **or**
      - `operator=SNCF`


  - for other pianos (**gray** on map): Same as above, but without `acess=public` or `operator=SNCF` tags

(overpass requests used to populate map are located in `overpass-requests` folder)

## Tags stats

Here is a taginfo link to compare usage of:
  - musical_instrument=piano
  - amenity=piano
  - musical_instrument:piano=yes

https://taginfo.openstreetmap.org/compare/musical_instrument=piano/amenity=piano/musical_instrument:piano=yes/

## TODO

This are informations to add via OSM tags

### Add more access infos

For the moment, there's no way to distinguish a bar with a place with a piano freely accessible and a place with a piano, but only reserved for concerts for example.
As the aim of the project is to quickly find on a map freely accessible pianos, it's an important point to decide.

What not using [access](http://wiki.openstreetmap.org/wiki/FR:Key:access) tag as it's used by the [toilets](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dtoilets) tag ?
For me its make sens to see:

  - *access=yes* explicitly public and open to whoever.
  - *access=permissive* while nominally private, no visible attempt is made to restrict access, and casual use appears to be tolerated by the owners.
  - *access=customers* while open to the public, the clear policy is to require a purchase prior to use. You may need a key or code to get in. Some people also use access=destination for this.

Of course, all that tags should only be used for nodes, not ways.

I'll make a proposal when it's more clear for me.

### Identify "real" pianos

It's always usefull to know whether a piano is a real one or a digital one.
For it we could use :
  - musical_instrument=piano
  - musical_instrument=digital_piano

### ~~Add all *pianos en gare* French project~~

~~The "pianos en gare" is a French project by the french railway service (SNCF) to place pianos in railways stations: http://www.sncf.com/fr/presse/carte/pianos-gares.
`operator=SNCF` is generally filled~~  => done (66 pianos added)

### Add infos when clicking

This is inherent to MapContrib evolutions, but it could be great to have some infos when clicking on a piano on the map:
  - place name
  - photo (if any)
  - "advanced" link to display all tags

=> See https://github.com/MapContrib/MapContrib/issues/130
