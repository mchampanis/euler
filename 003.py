#!/usr/bin/python3

n  = 600851475143
i  = 2

while i*i <= n:
  if n % i == 0:
    n = n // i
    print(i)
  else: 
    i += 1

if n != 1:
  print(n)

