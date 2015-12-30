#!/usr/bin/env python

import sys
from collections import defaultdict

result = defaultdict(float);
key_count = defaultdict(int);

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print line
    k1, v1 = line.split("\t")

    result[k1]+=float(v1);
    key_count[k1]+=1

    # split the line into columns
    #dir_num, service, line, date,  = k1.split(",")
    
for k,v in result.items():
    print k, '\t', v/key_count[k]