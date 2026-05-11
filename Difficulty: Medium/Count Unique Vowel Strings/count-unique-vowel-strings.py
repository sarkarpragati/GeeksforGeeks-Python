class Solution:
    def vowelCount(self, s):
        freq = {}

        for ch in s:
            if ch in "aeiou":
                freq[ch] = freq.get(ch, 0) + 1

        n = len(freq)

        if n == 0:
            return 0

        ways = 1

        for val in freq.values():
            ways *= val

        fact = 1
        for i in range(1, n + 1):
            fact *= i

        return ways * fact