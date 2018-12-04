cur = 0
with open("input.dat") as f:
  for line in f:
    cur += int(line)
print(cur)
