#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key,value = line.split("\t")

    # [derive mapper output key values]
    print '%s\t%s' % (key,value)