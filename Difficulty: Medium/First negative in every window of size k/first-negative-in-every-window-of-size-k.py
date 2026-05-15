#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        dq = deque()
        res = []
        
        # 1. Process the first window
        for i in range(k):
            if arr[i] < 0:
                dq.append(i)
        
        # 2. Process subsequent windows
        for i in range(k, n):
            # Record result for the current window
            if dq:
                res.append(arr[dq[0]])
            else:
                res.append(0)
            
            # Remove indices that are out of the next window
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # Add the new element's index if it's negative
            if arr[i] < 0:
                dq.append(i)
        
        # 3. Add result for the last window
        if dq:
            res.append(arr[dq[0]])
        else:
            res.append(0)
            
        return res
         # code here 
