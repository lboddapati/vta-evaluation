#!/usr/bin/env python

import sys
from collections import defaultdict
import glob   

stopslist_file = 'final_stops_list_final.txt'
freqcount_file = 'frequency_count.txt'

weekday_stops_freq_list = defaultdict(float)
weekend_stops_freq_list = defaultdict(float)
freqlist = defaultdict(float)

with open(freqcount_file) as fp:
#path = 'freq_output2/part*'   
#files=glob.glob(path) 
#for f in files:
#    with open(f) as fp:
        for line in fp:
            line = line.strip()
            key, freq = line.split('\t')
            key = key.strip()
            freq = float(freq.strip())
            freqlist[key] = freq


with open(stopslist_file) as fp:
    for line in fp:
        line = line.strip()
        stop, lineservice_list = line.split('\t')
        for lineservice in lineservice_list.strip('[]').split(','):
            lineservice = lineservice.strip().strip('\'')
            dir_num, service, bus_line, seq_no = lineservice.split(';')
            key = dir_num+';'+service+';'+bus_line
            count = freqlist[key]
            if int(service) == 1 :
                weekday_stops_freq_list[stop] += float(count)
            else :
                weekend_stops_freq_list[stop] += float(count)
                #print stop,"\t ::: ",service,"\t :::",weekend_stops_freq_list[stop]

for stop in weekday_stops_freq_list.keys():
    print stop,'\t',weekday_stops_freq_list[stop],'\t',weekend_stops_freq_list[stop]
