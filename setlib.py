import bitlib

def allMasksSizeK(k,arraysize):
'''
Returns a list of arraysize-bit integers with k bits raised
'''
	masks = []
	mask = (1 << k)-1
	while mask <= (1<<arraysize):
		masks.append(mask)
		mask = bitlib.nextGreatestSameBitcount(mask)
	return masks

def subset(array,mask):
'''
Returns a list with the subset of an array represented by a mask (where a raised x'th bit in the mask represents inclusion of the x'th element in the subset)
'''
	i = 0
	subset = []
	while mask > 0:
		if (mask & 1) == 1:
			subset.append(array[i])
		mask = mask >> 1
		i += 1
	return subset

#All non-empty subsets
def allSubsets(array, nullSet=False):
'''
Returns powerset (all subsets) of the given array as a list of lists. Set kwarg nullSet True to include empty set as an empty list.
'''
	length = len(array)
	mask = (1 << length) - 1
	subsets = []
	while mask > 0:
		subsets.append(subset(array,mask))
		mask -= 1
	if nullSet:
		subsets.append([])
	return subsets
powerset = allSubsets
pset = allSubsets

def allSubsetsSizeK(array,k):
'''
Return a list of all subsets with k elements.
'''
	leng = len(array)
	if k < 1 or k > leng:
		return []
	elif k == 1:
		return [[elt] for elt in array]
	elif k == leng:
		return [array]
	else:
		return [subset(array,mask) for mask in allMasksSizeK(k,leng)]

ksubset = allSubsetsSizeK
subsetk = allSubsetsSizeK

def allSubsetsKorSmaller(array,k):
'''
Return a list of all subsets with k or fewer elements.
'''
	subsets = []
	if k > len(array) or k < 1:
		return []
	else:
		for i in range(1,k+1):
			subsets += allSubsetsSizeK(array,i)
	return subsets

#wrapper function, strings don't support swapping elements
def nextPermutationString(strng):
'''
Return lexicographically-next string consisting of the same characters, -1 if there are no more permutations.
'''
	iterable = [c for c in strng]
	ans = nextPermutation(iterable)
	if ans == -1:
		return -1
	else:
		return ''.join(ans)

#returns -1 when no more permutations
def nextPermutation(iterable):
'''
Return next permuation of iterable, -1 if there are no more permutations
'''
	if not isinstance(iterable,list):
		
		if isinstance(iterable, (str, unicode)):
			return nextPermutationString(iterable)
		
		elif isinstance(iterable,tuple):
			return tuple(nextPermutation(list(iterable)))
		
		else:
			print "can't give nextPerm permutation for this type"
			exit(1)

	length = len(iterable)

	#How many elements at the end are in reverse sorted order. Let's call this the suffix
	# e.g. for list [1, 3, 5, 7, 9, 8, 6, 4, 2] the suffix includes
	# elements 9, 8, 6, 4, 2. The last element before the suffix, 7 will be 
	# swapped with an element from the suffix. Becuase we are considering
	# permutations that are greater, we choose the smallest element of the 
	# suffix that is greater than 7 - in this case 8 - and we swap these two
	# elements.

	#We now have the list [1, 3, 5, 8, 9, 7, 6, 4, 2], and a suffix
	# of 9 7 6 4 2, which is still in reverse sorted order.
	# To generate the 'smallest' permutation beginning with our prefix
	# 1,2,3,5,8, we simply reverse our suffix so that it is now in sorted order

	suffixIndex = length - 2
	while suffixIndex > -1 and (iterable[suffixIndex] >= iterable[suffixIndex+1]):
		suffixIndex -= 1

	if suffixIndex < 0: #happens when iterable is reverse sorted, or has length 0
		return -1
	else:
		prefixEnding = suffixIndex
		suffixIndex += 1

	while suffixIndex < length and iterable[suffixIndex] > iterable[prefixEnding]:
		suffixIndex+=1
	suffixIndex -= 1

	#Swap prefix-ending with smallest elt in the suffix that is bigger than prefix-ending
	temp = iterable[suffixIndex]
	iterable[suffixIndex], iterable[prefixEnding] = iterable[prefixEnding], iterable[suffixIndex]

	#return prefix as is, plus the descending-suffix reversed
	return iterable[0:prefixEnding+1] + iterable[prefixEnding+1:][::-1]

#Seriously consider how stringFlag and tupleFlag should be handled.
#Do they need to be keyword arguments?
def nextPermutationGenerator(iterable, allPermutations=False):
'''
Generator function for getting nextPermutation of iterable. Set kwarg allPermutations to True for all permutations starting from sorted order.
'''
	stringFlag = False
	tupleFlag = False
	if not isinstance(iterable,list):
		if isinstance(iterable, (str, unicode)):
			stringFlag = True
		elif isinstance(iterable,tuple):
			tupleFlag = True
		else:
			print "can't give nextPerm permutation for this type"
			exit(1)
	
	if allPermutations:
		iterable = sorted(iterable)
		if stringFlag: 
			#sorted(some_string) will return a list, we want a string
			iterable = ''.join(iterable)
	
	yield iterable #include self
	iterable = list(iterable)	
	while True:
		nextPerm = nextPermutation(iterable)
		if nextPerm == -1:
			return
		if stringFlag:
			yield ''.join(nextPerm)
		elif tupleFlag:
			yield tuple(nextPerm)
		else:
			yield nextPerm
		iterable = nextPerm

