class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLen = len(s)
        tLen = len(t)
        ans = ""
        if tLen > sLen:
            return ans

        m = sLen
        wordHash = makeHash(t)
        i, j = 0, tLen
        hashStr = makeHash(s[i:j])

        while True:
            temp = s[i:j]
            x = hashMatch(hashStr, wordHash)
            # print(temp,hashStr,x)
            if j == sLen and not x:
                break
            if x:
                if j-i <= m:
                    ans = temp
                    m = j-i
                hashStr[s[i]] -= 1
                i += 1
            else:
                if j <= sLen:
                    if s[j] not in hashStr:
                        hashStr[s[j]] = 1
                    else:
                        hashStr[s[j]] += 1
                    j += 1

        return ans


def makeHash(s):
    wordHash = {}
    for x in s:
        if x in wordHash:
            wordHash[x] += 1
        else:
            wordHash[x] = 1

    return wordHash


def hashMatch(a, b):
    for x in b:
        if not x in a:
            return False
        if b[x] > a[x]:
            return False
    return True
