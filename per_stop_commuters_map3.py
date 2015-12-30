#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()

    k1, v1 = line.split("\t");

    dir_num, service, line, date = k1.split(';')
    k2 = dir_num+";"+service+";"+line
    
    print k2,'\t',v1

