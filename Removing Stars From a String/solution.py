class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
      words1=makeUniqueCounts(word1)
      words2=makeUniqueCounts(word2)
      
      return words1==words2

def makeUniqueCounts(word):
  hashMap={}
  for i in word:
    if i in hashMap:
      hashMap[i]+=1
    else:
      hashMap[i]=1
  return [sorted(hashMap.keys()),sorted(hashMap.values())]
