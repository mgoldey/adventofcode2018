import sys

seen_pats = [0]
cur = 0

while True:
  seen_pats = sorted(seen_pats)
  with open("input.dat") as f:
    for line in f:
      cur += int(line)
      if cur in seen_pats:
        print(cur)
        sys.exit(0)
      else:
        seen_pats.append(cur)
