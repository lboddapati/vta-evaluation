#!/usr/bin/env python

import sys
from collections import defaultdict

result = defaultdict(list);

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    k, v = line.split("\t")
    result[k].append(v);

for key,values in result.items():
    print key,'\t',values

