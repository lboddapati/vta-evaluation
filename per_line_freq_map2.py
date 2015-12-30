#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    k1, v1 = line.split("\t")
    
    dir_num, service, line,date, = k1.split(";")
    k2= dir_num+";"+service+";"+line

    print '%s\t%s' % (k2, v1)
