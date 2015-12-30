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
        #print stops[index],'\t',prev_key
        print stops[index],'\t',prev_key+';'+`index`
