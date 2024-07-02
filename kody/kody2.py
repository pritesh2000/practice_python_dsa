# 2 check if given string is isomorphic to each other 

# Python3 program for the above approach
CHAR = 26

# This function returns true if
# str1 and str2 are isomorphic
def isoMorphic(str1, str2):
	n = len(str1)
	m = len(str2)
	
	# Length of both strings must be
	# same for one to one correspondence
	if n != m:
		return False
		
	
	# for counting the previous appearances of character
	# in both the strings
	countChars1 = [0] * CHAR
	countChars2 = [0] * CHAR
	
	# Process all characters one by one
	for i in range(n):
		countChars1[ord(str1[i]) - ord('a')] += 1
		countChars2[ord(str2[i]) - ord('a')] += 1
	
	# For string to be isomorphice the
	# previous counts of appearances of
	# current character in both string
	# must be same if it is not same
	# we return false
	for i in range(n):
		if countChars1[ord(str1[i]) - ord('a')] != countChars2[ord(str2[i]) - ord('a')]:
			return False
	
	return True

# Driver Code
print(int(isoMorphic("jjb", "xxy")))
print(int(isoMorphic("aab", "xyz")))

# This code is contributed by phasing17
