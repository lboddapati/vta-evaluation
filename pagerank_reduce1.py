#!/usr/bin/env python

import sys
from collections import defaultdict

stop_neighbourlist = defaultdict(list)
stop_ranks = defaultdict(float)

for line in sys.stdin:
    line = line.strip()

    src, src_rank, dest, dest_rank = line.split('\t')
    src = src.strip()
    dest = dest.strip()
    stop_neighbourlist[src].append(dest)
    stop_ranks[src] = float(src_rank.strip())

for stopname in stop_ranks.keys():
    print stopname,'\t',stop_ranks[stopname],'\t',stop_neighbourlist[stopname]
