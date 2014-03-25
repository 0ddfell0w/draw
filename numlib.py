from primelib import factorize

def greatestCommonDenominator(a,b):
	a,b = abs(a),abs(b)
	a,b = max(a,b), min(a,b)
	if b == 0 or b == a:
		return a
	else:
		return gcd(a % b, b)
gcd = greatestCommonDenominator

def eulersTotient(n):
	if n < 2:
		return 0
	pfactors = set(factorize(n))
	for x in pfactors:
		n -= (n / x)
	return n

totient = eulersTotient
phi = eulersTotient

def modularExponentiation(base,exponent,modulus):
	#normalize base
	base %= modulus
	if base < 0:
		base = modulus - base

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
