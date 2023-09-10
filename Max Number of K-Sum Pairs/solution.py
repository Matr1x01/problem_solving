class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans=0
        nums=sorted(nums)
        i,j=0,len(nums)-1
        while i<j:
            x=nums[i]+nums[j]
            if x==k:
                ans+=1
                i+=1
                j-=1
            elif x>k:
                j-=1
            else:
                i+=1
        return ans
            