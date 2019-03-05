#!/usr/bin/env python3
" Stores Grid class"

from cart import Cart
from location import Location


class Grid():
  r"""
  Example: example1.txt
    /----\
    |    |
    |    |
    \----/
  """
  grid = [[]]
  file = None
  carts = []
  crashes = []

  def __init__(self, *args, **kwargs):
    """
    >>> example1_grid = Grid(file="example1.txt")
    """

    # Set input from dicts
    for dictionary in args:
      if isinstance(dictionary, dict):
        for key in dictionary:
          setattr(self, key, dictionary[key])

    # Set input from kwargs
    for key in kwargs:
      setattr(self, key, kwargs[key])

    # In case of file input
    if self.file:
      with open(self.file) as input_grid_file:
        self.grid = input_grid_file.read()

    # re-initialize carts
    self.carts = []

    # Standardize as list of lists
    if isinstance(self.grid, str):
      self.grid = list(map(list, zip(*[list(_.strip()) for _ in self.grid.splitlines()])))
      # print(self.grid)
      # Now find all carts
      for irow, row in enumerate(self.grid):
        for icol, col in enumerate(row):

          # Carts always face either up (^), down (v), left (<), or right (>).
          if col in '><v^':

            self.carts.append(Cart(Location(irow, icol), col))

            # On your initial map, the track under each cart is a straight path matching the direction the cart is facing.
            self.grid[irow][icol] = '|' if col in "v^" else '-'

  def step(self):
    r"""
      Take a step in time.
      Carts all move at the same speed; 
        they take turns moving a single step at a time. 
      They do this based on their current location: 
        carts on the top row move first (acting from left to right), 
        then carts on the second row move (again from left to right), 
        then carts on the third row, and so on. 
      Once each cart has moved one step, the process repeats; each of these loops is called a tick.

      >>> example2_grid = Grid(file="example2.txt")
      >>> print(example2_grid)
      /----\
      |    |
      |    ^
      \----/
      >>> example2_grid.step() == 'OKAY'
      True
      >>> print(example2_grid)
      /----\
      |    ^
      |    |
      \----/
      >>> example2_grid.step() =='OKAY'
      True
      >>> print(example2_grid)
      /----<
      |    |
      |    |
      \----/
      >>> all(example2_grid.step()=='OKAY' for _ in range(5))
      True
      >>> print(example2_grid)
      v----\
      |    |
      |    |
      \----/
      """
    # loop over rows
    # loop over carts, from top to bottom (y) and from left to right (x)
    for cart in sorted(self.carts, key=lambda c: (c.location.y, c.location.x)):
      result = cart.move(self)

      # update
      if result == "CRASH":
        self.grid[cart.location.x][cart.location.y] = 'X'
        self.crashes.append(cart.location)
        return "CRASH"
    return "OKAY"

  def __repr__(self):
    r"""
    >>> example1_grid = Grid(file="example1.txt")
    >>> print(example1_grid)
    /----\
    |    |
    |    |
    \----/
    >>> example2_grid = Grid(file="example2.txt")
    >>> print(example2_grid)
    /----\
    |    |
    |    ^
    \----/

    """
    from copy import deepcopy

    # copy to output object
    output_grid = deepcopy(self.grid)

    # get carts
    for cart in self.carts:
      x, y = cart.location.x, cart.location.y
      output_grid[x][y] = str(cart) if output_grid[x][y] != 'X' else 'X'

    # flip syntax for x,y indexing
    output_grid = list(map(list, zip(*output_grid)))
    return "\n".join("".join(line) for line in output_grid)

  def __str__(self):
    " Alias for anything calling str instead of repr "
    return self.__repr__()


if __name__ == "__main__":
  import doctest
  doctest.testmod(raise_on_error=False, verbose=True)