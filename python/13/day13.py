#!/usr/bin/env python3

from grid import Grid


def part1():
  part1_grid = Grid(file="input.txt")
  while part1_grid.step() == "OKAY":
    pass
  print(part1_grid.crashes)


def part2():
  part2_grid = Grid(file="input.txt")
  while len(part2_grid.carts) > 1:
    part2_grid.step()
  print(part2_grid.carts[0].location)


def main():
  part1()
  part2()


if __name__ == "__main__":
  main()
