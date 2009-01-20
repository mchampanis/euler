#!/usr/bin/python3

# a^2 + b^2 = c^2
# a + b + c = 1000
# a < b < c
#
# subsituting and reducing:
# a = 1000(500 - b) / (1000 - b)

from math import sqrt

for b in range(1, 997):
	a = (1000 * (500 - b)) / (1000 - b)
	
	if int(a) == a and a > 0 and a < b:
		c = sqrt(a*a + b*b)		
		print("a = %d, b = %d, c = %d: abc = %d" % (a, b, c, a*b*c))
	