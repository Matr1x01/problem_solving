class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        m=min(len(word1),len(word2))
        for i in range(m):
            ans.append(word1[i])
            ans.append(word2[i])
        
        ans.append(word1[m:])
        ans.append(word2[m:])

        return ''.join(ans)
