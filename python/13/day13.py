#!/usr/bin/env python3

from grid import Grid


def part1():
  part1_grid = Grid(file="part1.txt")
  while part1_grid.step() == "OKAY":
    pass
  print(part1_grid.crashes)


def part2():
  pass


def main():
  part1()
  part2()


if __name__ == "__main__":
  main()
