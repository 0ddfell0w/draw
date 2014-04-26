def countBits(x):
'''
Count raised bits in integer x
'''
	ans = 0
	while x > 0:
		if (x & 1) == 1:
			ans += 1
		x = x >> 1
	return ans

def leastSignificant1(x):
'''
return power of 2 aligned with least significant raised bit
'''
	return x & (~x + 1)

# def leastSignificant0(x):
	# return x & (~x + 1)


def altCountBits(x):
'''
Count raised bits in integer x
'''
	ans = 0
	while x > 0:
		ans += 1
		x = leastSignificant1(x) ^ x
	return ans

def nextGreatestSameBitcount(v):
'''
Return next greatest integer with same number of raised bits
'''
	t = (v | (v - 1)) + 1;
	w = t | ((((t & -t) / (v & -v)) >> 1) - 1);
	#http://graphics.stanford.edu/~seander/bithacks.html
	# print bin(v),bin(w)#,bin(t)
	return w

