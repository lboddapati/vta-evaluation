#!/usr/bin/env python
import sys
from collections import defaultdict

for line in sys.stdin:
    line = line.strip()

    k1, v1 = line.split("\t")
    stops = dict()

    #print k1+":"
    for v in v1.strip('[]').split(","):
        v = v.strip().strip('\'"')
        #print '\t', v
        #seq, stopname, on, off = v.split(';')
        seq, on, off = v.split(';')
        seq = int(seq)
        on = int(on)
        off = int(off)
        if(stops.has_key(seq)):
            stops[seq] = [stops[seq][0]+on, stops[seq][1]+off]
        else:
            stops[seq] = [on, off]

    commuter_count = [0]*(max(stops.keys())+1)
    for i in range(1, len(commuter_count)):
        on, off = stops.get(i, [0,0])
        commuter_count[i] = abs(commuter_count[i-1]+on-off)
        #print "stop", i, "::",  commuter_count[i];

    dir_num, service, line, date, trip_id = k1.split(";")
    k2 = dir_num+";"+service+";"+line+";"+date
    #print k2, '\t', commuter_count
    print k2, '\t', commuter_count[1:]
        
    #print ""
    

