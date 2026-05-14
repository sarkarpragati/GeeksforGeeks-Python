class Solution:
	def preGreaterEle(self, arr):
	    n = len(arr)
        res = [-1] * n
        stack = []
        
        
        for i in range(n):
           
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            
            
            if stack:
                res[i] = stack[-1]
            
            
            stack.append(arr[i])
            
        return res