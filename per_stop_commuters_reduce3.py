#!/usr/bin/env python
import sys
from collections import defaultdict
#import numpy

result = defaultdict(list);
key_count = defaultdict(int);

for line in sys.stdin:
    line = line.strip()

    k, v = line.split("\t");

    new_commuter_count = []
    for c in v.strip('[]').split(','):
        new_commuter_count.append(float(c.strip()));

    old_commuter_count = result.get(k, None);
    if old_commuter_count is None:
        result[k] = new_commuter_count
    else:
        if(len(new_commuter_count) <= len(old_commuter_count)):
            #result[k] = old_commuter_count
            for i in range(0, len(new_commuter_count)):
                result[k][i] += new_commuter_count[i]

        elif(len(new_commuter_count) > len(old_commuter_count)):
            result[k] = new_commuter_count
            for i in range(0, len(old_commuter_count)):
                result[k][i] += old_commuter_count[i]

        #for i in range(0, min(len(new_commuter_count), len(old_commuter_count))):
        #    result[k][i] = old_commuter_count[i] + new_commuter_count[i]

    key_count[k] += 1

for key, val in result.items():
    #print key, '\t', numpy.array(val)/key_count[key]
    print key, '\t', [x/key_count[key] for x in val]

