class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        res = 1
        
        # Multiply numbers from 2 up to n
        for i in range(2, n + 1):
            res *= i
            
        return res
        