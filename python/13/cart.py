#!/usr/bin/env python3
" Stores Cart class"

from location import Location

# by convention, 0 is up, 90 is right, 180 is down, and 270 is left
orientation_dict = {'^': 0, '>': 90, 'v': 180, '<': 270}
reversed_orientation_dict = {value: key for key, value in orientation_dict.items()}

up = Location(x=0, y=-1)
down = Location(x=0, y=1)
right = Location(x=1, y=0)
left = Location(x=-1, y=0)


def check_for_crash(cart, grid):
  """
  Check crash conditions
  """
  grid_value = grid.grid[cart.location.x][cart.location.y]

  # off path
  not_a_valid_place_on_grid = grid_value == ' '

  # hit a wall perpendicularly
  hit_a_wall = (
    ((cart.orientation % 180) == 90 and grid_value == "|") or ((cart.orientation % 180) == 0 and grid_value == '-')
  )

  # hit another cart
  hit_another_cart = any([not (cart - other_cart) for other_cart in grid.carts if other_cart != cart])

  return not_a_valid_place_on_grid or hit_a_wall or hit_another_cart


class Cart():
  """
    This is a Cart object with a given state
    Key attributes:
      - turn_state (0,1,2)
      - orientation (nautical degrees)
      - location (Location class)
  """
  turn_state = 0
  crashed = False

  def __init__(self, location, orientation):
    """ 
    Carts always face either up (^), down (v), left (<), or right (>).
    """

    self.location = location
    self.orientation = orientation_dict[orientation]

  def turn(self):
    """
    Each time a cart has the option to turn (by arriving at any intersection), 
      it turns left the first time, 
      goes straight the second time, 
      turns right the third time, and then repeats ...
    """
    if self.turn_state == 0:
      self.orientation -= 90
    elif self.turn_state == 1:
      pass
    elif self.turn_state == 2:
      self.orientation += 90

    self.turn_state += 1

    self.orientation %= 360
    self.turn_state %= 3

  def move(self, grid):
    """
    Move based on orientation
    """
    if self.crashed:
      return "CRASH"

    if self.orientation == 0:
      self.location += up
    elif self.orientation == 180:
      self.location += down
    elif self.orientation == 90:
      self.location += right
    elif self.orientation == 270:
      self.location += left

    # check for curves
    grid_value = ''
    grid_value = grid.grid[self.location.x][self.location.y]

    if grid_value == '\\':
      # ^,v turn left; <,> turn right
      self.orientation += (-90 if self.orientation % 180 == 0 else +90)
      self.orientation %= 360
    if grid_value == '/':
      # ^,v turn right; <,> turn left
      self.orientation += (+90 if self.orientation % 180 == 0 else -90)
      self.orientation %= 360

    # check for intersections
    if grid_value == '+':
      self.turn()

    # check crash conditions
    if check_for_crash(self, grid):
      self.crashed = True

    return "CRASH" if self.crashed else "OKAY"

  def __repr__(self):
    return reversed_orientation_dict[self.orientation]

  def __sub__(self, other):
    return self.location - other.location


if __name__ == "__main__":
  import doctest
  doctest.testmod(raise_on_error=False, verbose=True)