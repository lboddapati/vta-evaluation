#!/usr/bin/env python
from collections import defaultdict

stopsweight_file = 'stopweights.txt'
stoppairs_file = 'stopslist.txt'

stops_weights = defaultdict(float)

with open(stopsweight_file) as fp:
    for line in fp:
        line = line.strip()
        stopname, weight = line.split("\t");
        stops_weights[stopname.strip()] = float(weight.strip())

with open(stoppairs_file) as fp:
    for line in fp:
        line = line.strip()
        stoppair, lines = line.split("\t");
        stoppair = stoppair.strip().strip('()')
        stopA, stopB = stoppair.split(',')
        stopA = stopA.strip().strip('\'')
        stopB = stopB.strip().strip('\'')
        print stopA,"\t",stops_weights[stopA],"\t",stopB,"\t",stops_weights[stopB]
        #print stopA,'\t',stopB
