#!/usr/bin/env python

import sys
import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    date, trip_id, block, vta_line, service, dir_num, direction, pattern, from_time, to_time,start_location, end_location, on, off, stop_id, ivr_num, stop_name, sequence = line.split(",")

    mm, dd, yy = date.strip().split(' ')[0].split('/')
    date = datetime.date(int(yy), int(mm), int(dd))
    key = vta_line+';'+str(date.isoweekday())
    value = on

    print '%s\t%s' % (key, value)
