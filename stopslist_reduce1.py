#!/usr/bin/env python

import sys
from collections import defaultdict
from datetime import datetime

result = defaultdict(list);
result2 = defaultdict(list);

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    k1, v1 = line.split("\t")

    #dir_num,service,line = k1.split(";")
    sequence,stop_name,date = v1.split(";")
    v2 = (int(sequence),stop_name,date)
    #k2 = (line,service,dir_num)

    #print v2[1]
    if v2 not in result[k1]:
       result[k1].append(v2);

for key,values in result.items():
    values.sort(key = lambda v:v[0])
    for vtemp in values:
      #if vtemp[1] not in result2[key]:
      #   result2[key].append(vtemp[1])
      if len(result2[key]) < vtemp[0]:
         result2[key].append(vtemp)
      else:
         temp = result2[key][vtemp[0]-1]
         if temp[1] != vtemp[1]:
            #print temp, vtemp
            vtemp_date = datetime.strptime(vtemp[2], "%m/%d/%Y %I:%M:%S %p")
            temp_date = datetime.strptime(temp[2], "%m/%d/%Y %I:%M:%S %p")
            if vtemp_date > temp_date :
                result2[key][vtemp[0]-1]=vtemp

for key,values in result2.items():
    #print '%s\t%s' % (key, values)
    print '%s\t%s' % (key, [x[1] for x in values])
    #print len(values)
