#!/usr/bin/env python3
import sys
from itertools import groupby
from operator import itemgetter
def read_input(f):
    for line in f:
        key, val = line.strip().split("\t")
        yield key, int(val)
data = read_input(sys.stdin)
for word, group in groupby(sorted(data, key=itemgetter(0)), key=itemgetter(0)):
    print(f"{word}\t{sum(v for _, v in group)}")
