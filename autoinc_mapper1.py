#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(",")

    # [derive mapper output key values]
    print '%s\t%s' % (data[2], (data[1],data[3],data[5]))