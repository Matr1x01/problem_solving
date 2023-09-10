class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list("aeiouAEIOU")
        indexes = []
        finds = []
        l = 0
        s = list(s)
        for i, val in enumerate(s):
            if val in vowels:
                l += 1
                indexes.append(i)
                finds.append(val)

        for i, val in enumerate(indexes):
            s[val] = finds[l-i-1]

        return "".join(s)
