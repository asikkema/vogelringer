#!/usr/bin/env python

import random
import sys
from itertools import combinations, product
import string

# The total number of rings put on a bird.
number_of_rings = 4

print '--Ringer code generator--'
if len(sys.argv) <= 2:
    print """
    Usage: python ringer.py <stationLetter-letter> <[ring-color-letters]>
    Example: python ringer.py M RLYB 500
    """
    sys.exit()

stationLetter = sys.argv[1]
letters = sys.argv[2]
ringLetters = stationLetter + letters

print 'generating for stationLetter %s with letters %s with max %s codes' % (stationLetter, letters, max)

def generateFor(combi):
    for length in xrange(1, len(combi)):
        for ring in map(''.join, product(*[combi]*length)):
            if len(ring) == number_of_rings and ring.count(stationLetter) == 1:
                yield ring 
            
rings = sorted(generateFor(ringLetters))
for ring in rings:
    print ring
