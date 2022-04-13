# python3 program for power set

import math

def powerSet(set,set_size):
	
	# set_size of power set of a set
	# with set_size n is (2**n -1)
	pow_set_size = (int) (math.pow(2, set_size))
	ans = []
	# Run from counter 000..0 to 111..1
	for counter in range(0, pow_set_size):
		l = []
		for j in range(0, set_size):
			
			# Check if jth bit in the
			# counter is set If set then
			# print jth element from set
			if((counter & (1 << j)) > 0):
				l.append(set[j])
		ans.append(l)
	return ans
	
# Driver program to test printPowerSet
set = ['a', 'b', 'c']
power_set = powerSet(set, 3)
print(power_set)

# This code is contributed by mits.

