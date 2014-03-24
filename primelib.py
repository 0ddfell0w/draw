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

def primesLessThanGenerator(n=1000):
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
