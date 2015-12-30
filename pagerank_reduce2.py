#!/usr/bin/env python

import sys
from collections import defaultdict

stop_neighbourlist = defaultdict(list)
old_ranks = defaultdict(float)
new_ranks = defaultdict(float)

for line in sys.stdin:
    line = line.strip()
    src, old_rank, partial_incontribution, partial_neighbours = line.split('\t')
    src = src.strip()
    old_rank = float(old_rank.strip())
    partial_incontribution = float(partial_incontribution.strip())
    partial_neighbours = partial_neighbours.strip().strip('[]').split(',')

    old_ranks[src] = old_rank
    new_ranks[src] += partial_incontribution

    for n in partial_neighbours:
        n = n.strip().strip('\'')
        #new_ranks[n] += partial_incontribution
        stop_neighbourlist[src].append(n)
        #print n#, new_ranks[n]

for stopname in old_ranks.keys():
    #if new_ranks[stopname] == 0:
    #    new_ranks[stopname] = old_ranks[stopname]
    print stopname,'\t',old_ranks[stopname],'\t',new_ranks[stopname],'\t',stop_neighbourlist[stopname]
        

