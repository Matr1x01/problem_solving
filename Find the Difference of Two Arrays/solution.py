class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1=makeHash(nums1)
        hash2=makeHash(nums2)
        ans1=[]
        for i in hash2:
            if i not in hash1:
                ans1.append(i)
        ans2=[]
        for i in hash1:
            if i not in hash2:
                ans2.append(i)

        return [ans2,ans1]


def makeHash(arr):
    hashMap={}
    for i in arr:
        if i in hashMap:
            hashMap[i]+=1
        else:
            hashMap[i]=0
    return hashMap
        