import numlib
from random import randrange

def isPrime(n):
	'''
	True if n is prime, else False
	'''
	if n < 2:
		return False
	if n%2 == 0:
		return n == 2
	i = 3
	while i*i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

def primesLessThan(n):
	'''
	Returns a list of primes less than n. Implements a half sieve
	'''
	if n < 3:
		return []
	else:
		primes = [2]
		oddsListsize = n/2
		oddsList = [1]*oddsListsize

		value = 3
		idx = lambda value: (value - 3) / 2

		while value < n:
			if oddsList[idx(value)] == 0:
				pass
			else:
				primes.append(value)
				valueRunner = value*value
				while valueRunner < n:
					oddsList[idx(valueRunner)] = 0
					valueRunner += 2*value
			value += 2

		return primes

primes = primesLessThan

#implements a half sieve.
def primesLessThanGenerator(n=1000):
	'''
	Generator for primes less than n using half sieve, n defaults to 1000
	'''
	if n < 0:
		n *= -1
	if n < 3:
		return
	else:
		yield 2
		primes = [2]
		oddsListsize = n/2
		oddsList = [1]*oddsListsize

		value = 3
		idx = lambda value: (value - 3) / 2

		while value < n:
			if oddsList[idx(value)] == 0:
				pass
			else:
				yield value
				valueRunner = value * value
				while valueRunner <= n:
					oddsList[idx(valueRunner)] = 0
					valueRunner += 2 * value
			value += 2
		return

primegen = primesLessThanGenerator
gen = primesLessThanGenerator

def primeFactorization(n):
	pfactors = []
	if n < 0:
		n *= -1
	if n == 1:
		return pfactors
	primes = primesLessThanGenerator(n+1)
	while True:
		nextPrime = next(primes)
		while n % nextPrime == 0:
			pfactors.append(nextPrime)
			n /= nextPrime
		if n == 1:
			return pfactors

factorization = primeFactorization
factorize = primeFactorization

# Returns True if candidate is probably prime
# Returns False if candidate is definitely composite
def fermatPrimeTest(candidate,trials=3):
	'''
	Probabilistic primality test (Fermat's) using modular exponentiation. Returns False if definitely composite, True if probably prime.
	'''
	if candidate < 4:
		return (candidate > 1)
	elif candidate & 1 == 0:
		return False
	else:
		for trial in xrange(trials):
			randomBase = randrange(2,candidate)
			exponent = candidate - 1
			modulus = candidate
			if numlib.modularExponentiation(randomBase,exponent,modulus) != 1:
				return False
		return True


fermat = fermatPrimeTest
isProbablyPrime = fermatPrimeTest
