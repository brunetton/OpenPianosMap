#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Check number of pianos in "pianos en gare" project to monitor potential new pianos.
http://www.sncf.com/fr/presse/carte/pianos-gares
'''

from urllib import urlopen
from xml.dom.minidom import parseString


KML_URL = 'https://www.google.com/maps/d/kml?mid=1lL6Ylpo7P3HnANcHTAzbH5hEx-E&forcekml=1'
KNOWN_PIANOS_NB = 76

data = urlopen(KML_URL).read()
dom = parseString(data)
nb_pianos = len(dom.getElementsByTagName('Point'))
if nb_pianos > KNOWN_PIANOS_NB:
    print "=> NEW pianos to map !  :)"
elif nb_pianos < KNOWN_PIANOS_NB:
    print "=> Strange: less pianos  :("
else:
    print "number of pianos: still {}. Nothing new.".format(nb_pianos)
