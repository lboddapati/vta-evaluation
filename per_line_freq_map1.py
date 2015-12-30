#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into columns
    date, trip_id, block, line, service, dir_num, direction, pattern, from_time, to_time,start_location, end_location, on, off, stop_id,ivr_num, stop_name, sequence = line.split(",")
    key = dir_num+";"+service+";"+line+";"+date
    value = trip_id#+";"+sequence

    print '%s\t%s' % (key, value)
