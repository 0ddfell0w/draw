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