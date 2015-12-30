#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into columns
    prev_key,prev_value= line.split("\t")
    prev_value = prev_value.replace("[", "")
    prev_value = prev_value.replace("]", "")
    prev_value = prev_value.replace("'", "")
    prev_value = prev_value.replace(", ", ",")
    stops = prev_value.split(",")

    for index in range(len(stops)):

        if index == 0:
           prev_stop = stops[index]
        else:
           new_stop = stops[index]
           keym2 = prev_stop,new_stop
           valm2 = prev_key
           prev_stop = new_stop

           print keym2,'\t',valm2
