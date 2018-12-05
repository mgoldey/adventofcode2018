#!/usr/bin/env python3
from collections import defaultdict


def hash_string(input_string):
  freq = defaultdict(lambda: 0)
  for char in input_string:
    freq[char] += 1
  return freq


twos, threes = 0, 0
with open("input.dat") as f:
  for line in f:
    h = hash_string(line.strip())
    twos += int(2 in h.values())
    threes += int(3 in h.values())
print(twos * threes)
