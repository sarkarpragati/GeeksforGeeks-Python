class Solution:
    def longestUniqueSubstr(self, s):
        char_map = {}
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            # If character is already in the map, move 'left' pointer
            # to the right of the previous occurrence
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            
            # Update the last seen index of the character
            char_map[s[right]] = right
            
            # Update max_len with the current window size
            max_len = max(max_len, right - left + 1)
            
        return max_len