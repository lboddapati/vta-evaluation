#!/usr/bin/env python

import sys
from collections import defaultdict

result = defaultdict(list);

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print line
    k1, v1 = line.split("\t")

    k1 = k1.strip();
    trip_id  = v1.strip();
    #trip_id, sequence  = v1.split(";")
    #sequence = int(sequence)
    #if sequence == 1:
    #    result[k1]+=1
    if trip_id not in result[k1]:
        result[k1].append(trip_id)


for key,trips in result.items():
        print key, '\t',len(trips)
