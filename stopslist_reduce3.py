#!/usr/bin/env python
import sys
from collections import defaultdict

red3result = defaultdict(list);

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    stop_name,dirSerLine= line.split("\t")
    if dirSerLine not in red3result[stop_name]:
      red3result[stop_name].append(dirSerLine);

for key,values in red3result.items():
    print key,'\t',values
