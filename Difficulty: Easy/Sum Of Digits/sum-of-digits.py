class Solution:
    def sumOfDigits(self, n):
        digit_sum = 0
        
        while n > 0:
            # Extract the last digit using modulo 10
            digit_sum += n % 10
            
            # Remove the last digit using floor division
            n //= 10
            
        return digit_sum
        