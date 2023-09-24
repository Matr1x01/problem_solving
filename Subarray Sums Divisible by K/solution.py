class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans,s=0,0
        modHash={}
        modHash[0]=1
        for i in nums:
            s+=i
            m=s%k
            if m<0:
                m=k-m
            if m in modHash:
                ans+=modHash[m]
                modHash[m]+=1
            else:
                modHash[m]=1


        return ans
        

