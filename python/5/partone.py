#!/usr/bin/env python3
polymer = []
with open("input.dat") as f:
  while True:
    new_char = f.read(1)
    if not new_char or new_char == '\n':
      break
    if len(polymer) > 0:
      if polymer[-1].upper() == new_char.upper() and polymer[-1] != new_char:
        polymer.pop()
      else:
        polymer.append(new_char)
    else:
      polymer.append(new_char)
print(len(polymer))
