import primelib

def greatestCommonDenominator(a,b):
	'''
	Euclid's algorithm for greatest common denominator
	'''
	a,b = abs(a), abs(b)
	a,b = max(a,b), min(a,b)
	if b == 0 or b == a:
		return a
	else:
		return gcd(a % b, b)

gcd = greatestCommonDenominator


def coprime(a,b):
	'''
	Return True if and b are relatively prime (ie gcd(a.b) == 1), else false
	'''
	return (greatestCommonDenominator(a,b) == 1)

isCoprime = coprime
relativelyPrime = coprime
relprime = coprime


def leastCommonMultiple(a,b):
	'''
	return least common multiple, 0 if a == b == 0
	'''
	if a == b == 0:
		return 0
	else:
		return (a * b) / greatestCommonDenominator(a,b)

lcm = leastCommonMultiple

def eulersTotient(n):
	'''
	return number of integers i, 0 < i < n, that are coprime with n
	'''
	if n < 2:
		return 0
	primeFactors = set(primelib.factorize(n))

#	given prime factor x of n, (n/x) many integers between 1 and n are also divisble
#	by x and therefor not coprime with n
	for x in primeFactors:
		n -= (n / x)
	return n

totient = eulersTotient
phi = eulersTotient


def modularExponentiation(base,exponent,modulus):
	'''
	return result of modular exponentiation by squaring
	'''
	#normalize base
	base %= modulus
	print base,
	print base
	powerOfBase = base
	product = 1
	while exponent > 0:
		if (exponent & 1) == 1:
			product *= powerOfBase
			product %= modulus

		exponent = (exponent >> 1)
		powerOfBase = (powerOfBase*powerOfBase)%modulus
	return product

modExp = modularExponentiation
expMod = modularExponentiation
