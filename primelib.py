from numlib import modularExponentiation
from random import randrange

def isPrime(n):
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

#implements a half sieve. OddsList represents integers from [3,n)
def primesLessThan(n):
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
	# for x in primesLessThanGenerator(n+1):
	primes = primesLessThanGenerator(n+1)
	while True:
		nextPrime = next(primes)
		while n % nextPrime == 0:
			pfactors.append(nextPrime)
			n /= nextPrime
		if n == 1:
			return pfactors

factorization = primeFactorization
factorize = factorization

# Returns True if candidate is probably prime
# Returns False if candidate is definitely composite
def fermatPrimeTest(candidate,trials=3):
	if candidate < 4:
		return (candidate > 1)
	else:
		for trial in xrange(trials):
			randomBase = randrange(2,candidate)
			exponent = candidate - 1
			modulus = candidate
			if modularExponentiation(randomBase,exponent,modulus) != 1:
				return False
		return True


fermat = fermatPrimeTest
isProbablyPrime = fermatPrimeTest

