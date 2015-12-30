#!/usr/bin/env python

import sys
from collections import defaultdict

stop_neighbourlist = defaultdict()
old_ranks = defaultdict(float)
in_contributions = defaultdict(float)

for line in sys.stdin:
    line = line.strip()
    src, old_rank, neighbours = line.split('\t')
    src = src.strip()
    old_rank = float(old_rank.strip())
    stop_neighbourlist[src] = neighbours.strip()
    neighbours = neighbours.strip().strip('[]').split(',')

    old_ranks[src] = old_rank

    out_contribution = old_rank/len(neighbours)
    for n in neighbours:
        n = n.strip().strip('\'')
        in_contributions[n] += out_contribution
        #print n, in_contributions[n]

for stopname in old_ranks.keys():
    print stopname,'\t',old_ranks[stopname],'\t',in_contributions[stopname],'\t',stop_neighbourlist[stopname]
        
