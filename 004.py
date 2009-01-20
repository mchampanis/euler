#!/usr/bin/python3

def is_palindrome(n):
  s = str(n)

  if s == s[::-1]:
    return True
  else:
    return False

max = 0

# palindrome is made up of digits "ABCCBA"
# so:
# 100 000a + 10 000b + 1 000c + 100c + 10b + 1a
# 100 001a + 10 010b + 1100c
# 11(9091a + 910b + 100c)
#
# 11 is prime, one of the numbers must be divisible by 11
# 990 is the smallest number below 999 divisible by 11

for i in range(990, 99, -11):
  for j in range(999, 99, -1):
    p = i * j

    if is_palindrome(p) and p > max:
      max = p

print(max)
    
