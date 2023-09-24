class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap={}
        for i in strs:
            x=''.join(sorted(list(i)))
            if x in hashMap:
                hashMap[x].append(i)
            else:
                hashMap[x]=[i]
        
        return hashMap.values()