from bitlib import nextGreatestSameBitcount
nextMaskGreater = nextGreatestSameBitcount

def allMasksSizeK(k,arraysize):
	masks = []
	mask = (1 << k)-1
	while mask <= (1<<arraysize):
		masks.append(mask)
		mask = nextGreatestSameBitcount(mask)
	return masks

def subset(array,mask):
	i = 0
	subset = []
	while mask > 0:
		if (mask & 1) == 1:
			subset.append(array[i])
		mask = mask >> 1
		i += 1
	return subset

def allSubsets(array):
	length = len(array)
	mask = (1 << length) - 1
	subsets = []
	while mask > 0:
		subsets.append(subset(array,mask))
		mask -= 1
	return subsets
powerset = allSubsets
pset = allSubsets

def allSubsetsSizeK(array,k):
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
	subsets = []
	if k > len(array) or k < 1:
		return []
	else:
		for i in range(1,k+1):
			subsets += allSubsetsSizeK(array,i)
	return subsets

#wrapper function, strings don't support swapping elements
def nextPermutationString(strng):
	iterable = [c for c in strng]
	ans = nextPermutation(iterable)
	if ans == -1:
		return -1
	else:
		return ''.join(ans)

#returns -1 when no more permutations
def nextPermutation(iterable):
	if not isinstance(iterable,list):
		if isinstance(iterable, (str, unicode)):
			return nextPermutationString(iterable)
		if isinstance(iterable,tuple):
			return tuple(nextPermutation([x for x in iterable]))
		else:
			print "can't give next permutation for this type"
			exit(0)
	length = len(iterable)
	suffixIndex = length - 2
	while suffixIndex > -1 and iterable[suffixIndex] >= iterable[suffixIndex+1]:
		suffixIndex -= 1
	if suffixIndex < 0: #happens when iterable is reverse sorted, or has length 0
		return -1
	prefixEnding = suffixIndex
	suffixIndex += 1
	while suffixIndex < length and iterable[suffixIndex] > iterable[prefixEnding]:
		suffixIndex+=1
	suffixIndex -= 1

	#Swap prefix-ending for smallest elt bigger than prefix-ending in the suffix
	temp = iterable[suffixIndex]
	iterable[suffixIndex] = iterable[prefixEnding]
	iterable[prefixEnding] = temp

	#return ascending prefix plus the descending suffix reversed
	return iterable[0:prefixEnding+1] + iterable[prefixEnding+1:][::-1]

