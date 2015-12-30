#!/usr/bin/env python

import sys
from collections import defaultdict

#commuters_per_line_weekday = defaultdict(tuple);
commuters_per_line_weekday = defaultdict(int);

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t') 
    key = key.strip();
    comm = int(value.strip())

    #tup = commuters_per_line_weekday.get(key, None)
    #if(tup is None):
    #    tup = (comm, 1)
    #else :
    #    tup = (tup[0]+comm, tup[1]+1)
    #commuters_per_line_weekday[key] = tup
    commuters_per_line_weekday[key] += comm

for k2, v2 in commuters_per_line_weekday.items():
    #print '%s\t%s' % (k2, v2[0]/v2[1])
    print '%s\t%s' % (k2, v2)

