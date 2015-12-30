#!/usr/bin/env python
from collections import defaultdict

commuters_file = 'commuters_count.txt'
stopslist_file = 'final_stops_list_final.txt'

weekday_stops_commuters_list = defaultdict(float)
weekend_stops_commuters_list = defaultdict(float)
commuterslist = defaultdict(list)

with open(commuters_file) as fp:
    for line in fp:
        line = line.strip()
        key, commuters = line.split('\t')
        key = key.strip()
        for comm in commuters.strip('[]').split(','):
            comm = float(comm.strip())
            commuterslist[key].append(comm)

with open(stopslist_file) as fp:
    for line in fp:
        line = line.strip()
        stop, lineservice_list = line.split('\t')
        for lineservice in lineservice_list.strip('[]').split(','):
            lineservice = lineservice.strip().strip('\'')
            dir_num, service, bus_line, seq_no = lineservice.split(';')
            key = dir_num+';'+service+';'+bus_line
            count = commuterslist[key][int(seq_no)]
            if int(service) == 1 :
                weekday_stops_commuters_list[stop] += float(count)
            else :
                weekend_stops_commuters_list[stop] += float(count)

for stop in weekday_stops_commuters_list.keys():
    print stop,'\t',weekday_stops_commuters_list[stop],'\t',weekend_stops_commuters_list[stop]
