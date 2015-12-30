#!/usr/bin/env python

import sys
from collections import defaultdict

commuters_per_line_service_month = defaultdict(int);

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t')

    vta_line, month, service = key.strip().split(';')
    #if int(service) == 1:
    #    k2 = vta_line+';'+month+';'+'weekday'
    #else:
    #    k2 = vta_line+';'+month+';'+'non-weekday'
    k2 = key
    v2 = int(value.strip())
    commuters_per_line_service_month[k2] += v2


for k2, v2 in commuters_per_line_service_month.items():
    print '%s\t%s' % (k2, v2)
