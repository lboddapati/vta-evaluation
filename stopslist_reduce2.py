#!/usr/bin/env python

import sys
from collections import defaultdict

red2result = defaultdict(list);

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    stop_pair,prev_value= line.split("\t")
    direction,service,line= prev_value.split(";")
    new_value = direction,line
    if prev_value not in red2result[stop_pair]:
      red2result[stop_pair].append(new_value);

for key,values in red2result.items():
    print key,'\t',values
