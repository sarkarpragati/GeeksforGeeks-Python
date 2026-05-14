class Solution:
	def prevSmaller(self, arr):
	
        n = len(arr)
        res = [-1] * n
        stack = []
        
        # Traverse from left to right
        for i in range(n):
            # Pop elements that are not smaller than the current element
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            
            # If stack is not empty, the top element is the PSE
            if stack:
                res[i] = stack[-1]
            
            # Push the current element onto the stack
            stack.append(arr[i])
            
        return res