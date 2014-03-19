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

def primegen(primes=[]):
	yield 2
	yield 3
	x = 6
	# if primes = []:
	while True:
		if isPrime(x-1):
			yield x - 1
		if isPrime(x+1):
			yield x + 1
		x += 6
	# else:
	# 	return

#The point of this primes parameter is to perhaps check
#if x is in a list of primes we've already computed, instead
#of checking the factors over and over again
pg = primegen
gen = primegen


#Implements a half-sieve
def primesLessThan(n):
	if n < 3:
		return []
	else:
		primes = [2]
		oddsListsize = n/2
		oddsList = [1]*oddsListsize
		realValue = 3
		while realValue < n:
			index = (realValue-3) / 2
			if oddsList[index] == 0:
				pass
			else:
				if isPrime(realValue):
					valueRunner = realValue*realValue				
				#This isn't obvious, but we've already dealt with
				#any multiples of realValue below realValue squared
					
					while valueRunner < n:
						indexRunner = (valueRunner-3)/2
						oddsList[indexRunner] = 0
						valueRunner += 2*realValue
			realValue += 2
		for x in range(0,oddsListsize-1):
			if oddsList[x] == 1:
				primes.append(2*x+3)
		return primes


def primegen(primes=[]):
	yield 2
	yield 3
	x = 6
	# if primes = []:
	while True:
		if isPrime(x-1):
			yield x - 1
		if isPrime(x+1):
			yield x + 1
		x += 6
	# else:
	# 	return

#The point of this primes parameter is to perhaps check
#if x is in a list of primes we've already computed, instead
#of doing trial division over and over again
pg = primegen
gen = primegen

