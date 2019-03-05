#!/usr/bin/env python3

from grid import Grid
from copy import deepcopy


def test_two_cars():
  " test two cars on a loop that don't crash "
  g = Grid(file="example3.txt")
  orig_g = deepcopy(g)

  # loop once
  assert all(g.step() == 'OKAY' for _ in range(8))
  assert str(g) == str(orig_g)


def test_crash():
  g = Grid(file="simple_crash.txt")
  while g.step() == "OKAY":
    pass
  assert g.crashes.__repr__() == '[(0, 3)]'
