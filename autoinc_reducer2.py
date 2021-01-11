#!/usr/bin/env python

import sys

accident_count = {}

def flush():
    for key in accident_count.keys():
        print '%s\t%s' % (key,accident_count[key])

for line in sys.stdin:
    line = line.strip()
    make_year, acc_count = line.split('\t')
    acc_count = int(acc_count.replace("'","").replace("(","").replace(")",""))

    # if vin is not present in the dictionary create a new entry
    if make_year not in accident_count:
        accident_count[make_year] = 0

    accident_count[make_year] += acc_count

# [output the reducer key values]
flush()