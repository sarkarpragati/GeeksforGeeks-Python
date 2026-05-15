#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n = len(s)
        res = []
        
        # Total number of subsequences is 2^n
        # We start from 1 to avoid the empty subsequence
        total_subsequences = 1 << n  # This is 2^n
        
        for i in range(1, total_subsequences):
            current_sub = ""
            for j in range(n):
                # Check if the j-th bit is set in i
                if (i & (1 << j)):
                    current_sub += s[j]
            
            res.append(current_sub)
        
        # Sort the results lexicographically as required
        res.sort()
        return res