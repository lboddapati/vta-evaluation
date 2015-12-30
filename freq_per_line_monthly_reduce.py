#!/usr/bin/env python

import sys
from collections import defaultdict

freq_per_line_service_month = defaultdict(list);

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t')

    #vta_line, month, service = key.strip().split(';')
    #if int(service) == 1:
    #    k2 = vta_line+';'+month+';'+'weekday'
    #else:
    #    k2 = vta_line+';'+month+';'+'non-weekday'
    k2 = key
    v2 = int(value.strip())

    if v2 not in freq_per_line_service_month[k2]:
        freq_per_line_service_month[k2].append(v2)


for k2, v2 in freq_per_line_service_month.items():
    print '%s\t%s' % (k2, len(v2))
