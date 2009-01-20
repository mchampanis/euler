#!/usr/bin/python3
# TODO: better solution

numbers = list(range(1,21))

for x in range(20, 0, -1):
  for y in range(2, 21):
    if x != y and x % y == 0:
      if y in numbers:
        numbers.remove(y)

max   = max(numbers)
look  = True
i     = 0

while look:
  i += max

  good = True

  for n in numbers:
    if i % n != 0:
      good = False
      break

  if good:
    look = False

print(i)
