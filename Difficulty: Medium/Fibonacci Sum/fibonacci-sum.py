#User function Template for python3

class Solution:
    def fibSum(self, n):
        #code here
        if n == 0: return 0
        if n == 1: return 1
        
        MOD = 1000000007
        
        # We need f(n+2) to use the formula: Sum = f(n+2) - 1
        # We calculate up to the (n+2)th Fibonacci number
        a, b = 0, 1
        for i in range(2, n + 3):
            a, b = b, (a + b) % MOD
            
        # The sum is f(n+2) - 1
        # We add MOD before subtracting to handle negative results
        return (b - 1 + MOD) % MOD