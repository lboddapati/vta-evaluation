#!/usr/bin/env python

import sys

delta = 1.e-4
halt = True

for line in sys.stdin:
    line = line.strip()
    src, old_rank, new_rank, neighbours = line.split('\t')
    old_rank = float(old_rank.strip())
    new_rank = float(new_rank.strip())
    #print abs(old_rank - new_rank)
    if abs(old_rank - new_rank) > delta :
        halt = False

print halt
