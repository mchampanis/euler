#!/usr/bin/python3

def sum_of_squares(n):
  return ((n) * (n + 1) * (2*n + 1)) // 6

def sum(n):
  return (n * (n + 1)) // 2

n = 100

print(sum(n) * sum(n) - sum_of_squares(n))
