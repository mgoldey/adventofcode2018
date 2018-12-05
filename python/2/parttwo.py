#!/usr/bin/env python3
import sys
import editdistance
data=open("input.dat").read().splitlines()

for line1 in data:
  for line2 in data:
    if line1==line2 or len(line1)!=len(line2):
      continue
    if editdistance.eval(line1,line2)==1:
      print("".join(i for i,j in zip(line1,line2) if i==j))
      sys.exit(1)
