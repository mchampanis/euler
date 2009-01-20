#!/usr/bin/python3

def is_prime(n, p):
  if n == 1 or n % 2 == 0 or n % 3 == 0:
    return False

  for i in p:
    if i * i > n:
      break
    
    if n % i == 0:
      return False
  
  return True

c = 10001
p = [2, 3]
n = 1
i = 0

while i <= c:
  if is_prime(n, p):
    p.append(n)
    i += 1
  
  n += 2

print(p[c - 1])

