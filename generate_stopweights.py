#!/usr/bin/env python

import sys
from collections import defaultdict

commuter_count = 'total_commuters.txt'
freq_count = 'total_frequency.txt'
freqlist = defaultdict(tuple)
comlist = defaultdict(tuple)
final_list = defaultdict(float)
running_count = 0
weekday_weight = float(5)/7
weekend_weight = float(2)/7


with open (freq_count) as fre:
    for line in fre:
        line = line.strip()
        stopname, weekday_freq, weekend_freq = line.split('\t')
        stopname = stopname.strip()
        weekday_freq = float(weekday_freq.strip())
        weekend_freq = float(weekend_freq.strip())
        freqlist[stopname] = (weekday_freq, weekend_freq)

with open (commuter_count) as com:
    for line in com:
        line = line.strip()
        stopname, weekday_commuters, weekend_commuters = line.split('\t')
        stopname = stopname.strip()
        weekday_commuters = float(weekday_commuters.strip())
        weekend_commuters = float(weekend_commuters.strip())
        comlist[stopname] = (weekday_commuters, weekend_commuters)

for stopname in comlist.keys():
    weight = 0
    comm = float(comlist[stopname][0])
    freq = float(freqlist[stopname][0])
    if(comm!=0 and freq !=0):
        weight += weekday_weight * comm/freq
        #print stopname, comm, freq, weight
        
    comm = float(comlist[stopname][1])
    freq = float(freqlist[stopname][1])
    if(comm!=0 and freq !=0):
        weight += weekend_weight * comm/freq

    final_list[stopname] = weight
    running_count += final_list[stopname]
        
for stopname, weight in final_list.items():         
    print stopname,'\t',(weight/running_count)

#for stopname, weight in final_list.items():
#    print stopname,'\t',freqlist[stopname],'\t',comlist[stopname],'\t',weight
