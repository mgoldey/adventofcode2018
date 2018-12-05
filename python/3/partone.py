#!/usr/bin/env python3

from collections import defaultdict
fabric = defaultdict(lambda: defaultdict(lambda: 0))
with open("input.dat") as f:
  for line in f:
    x, y, lx, ly = list(
      map(int,
          line.replace("@", "").replace(":", "").replace(",", " ").replace("x", " ").split()[1:])
    )
    for ix in range(x, x + lx):
      for iy in range(y, y + ly):
        fabric[ix][iy] += 1

shared = 0
for row in fabric.values():
  for col in row.values():
    if col > 1:
      shared += 1
print(shared)
