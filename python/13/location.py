#!/usr/bin/env python3
" Stores Location class"


class Location():
  " stores x,y coords "

  def __init__(self, x, y):
    """
    >>> point = Location(0, 0)
    """
    self.x = x
    self.y = y

  def __sub__(self, other):
    """
    Returns taxicab distance metric
    >>> point = Location(0, 0)
    >>> point2 = Location(5, 1)
    >>> print(point2-point)
    6
    """
    return abs(self.x - other.x) + abs(self.y - other.y)

  def __add__(self, other):
    """
    >>> point = Location(1, 2)
    >>> point2 = Location(5, 1)
    >>> print(point+point2)
    (6, 3)
    """
    return Location(self.x + other.x, self.y + other.y)

  def __iadd__(self, other):
    """
    >>> point = Location(3, 4)
    >>> point2 = Location(5, 1)
    >>> point+=point2
    >>> print(point)
    (8, 5)
    """
    self.x += other.x
    self.y += other.y
    return self

  def __repr__(self):
    """
    >>> point = Location(0, 0)
    >>> print(point)
    (0, 0)
    """
    return ("({}, {})".format(self.x, self.y))


if __name__ == "__main__":
  import doctest
  doctest.testmod(raise_on_error=False, verbose=True)