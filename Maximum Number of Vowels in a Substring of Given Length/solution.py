class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(list("aeiouAEIOU"))
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        m = count
        i = 1
        while i+k <= len(s):
            count -= (1 if s[i-1] in vowels else 0)
            count += (1 if s[i+k-1] in vowels else 0)
            m = max(m, count)
            i += 1

        return m
