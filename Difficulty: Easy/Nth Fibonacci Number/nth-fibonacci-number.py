class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        # Variables to store the previous two Fibonacci numbers
        prev2, prev1 = 0, 1
        
        # Iteratively calculate from 2 up to n
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1
