#!/usr/bin/python3

def fib(n):
  n2, n1 = 0, 1

  for i in range(n):
    n2, n1 = n1, n1 + n2
  
  return n1

total, i, f = 0, 0, 0

while f < 4000000:
  i += 1
  f = fib(i)
  
  if f % 2 == 0:
    total += f

print(total)
