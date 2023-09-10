class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sz = len(words[0])
        l = len(words)
        windowSz = sz*l
        wordHash = {}
        for x in words:
            if x in wordHash:
                wordHash[x] += 1
            else:
                wordHash[x] = 1

        ans = []

        for i in range(0, len(s)-windowSz+1):
            x = (s[i:i+windowSz])
            if hashMatch(makeHash(x, sz, windowSz), wordHash):
                ans.append(i)

        return ans


def makeHash(s, sz, window):
    ans = {}
    for i in range(0, window-sz+1, sz):
        x = s[i:i+sz]
        if x in ans:
            ans[x] += 1
        else:
            ans[x] = 1

    return ans


def hashMatch(a, b):
    for x in b:
        if not x in a:
            return False
        if b[x] != a[x]:
            return False
    return True
