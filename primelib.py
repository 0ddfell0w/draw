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