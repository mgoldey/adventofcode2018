#!/usr/bin/env python3

import string


def extra_filter(bad_char):
  polymer = []
  with open("input.dat") as f:
    while True:
      new_char = f.read(1)
      if not new_char or new_char == '\n':
        break
      if new_char.lower() == bad_char:
        continue
      if len(polymer) > 0:
        if polymer[-1].upper() == new_char.upper() and polymer[-1] != new_char:
          polymer.pop()
        else:
          polymer.append(new_char)
      else:
        polymer.append(new_char)
  return len(polymer)


letters = string.ascii_letters[:26]
min_polymer = list(map(extra_filter, letters))
print(min(min_polymer))
