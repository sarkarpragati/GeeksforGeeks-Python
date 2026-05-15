class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n = len(arr)
        if n < k:
            return 0
        
        # Step 1: Calculate sum of the first window of size k
        current_sum = sum(arr[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window across the array
        for i in range(k, n):
            # Add the new element and remove the first element of the previous window
            current_sum += arr[i] - arr[i - k]
            
            # Step 3: Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum