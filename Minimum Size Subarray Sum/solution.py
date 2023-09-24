class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,1
        ans=1000000
        flag=False
        l=len(nums)
        x=sum(nums[i:j])
        while i<j:   
            if x>=target:
                flag=True
                ans=min(ans,j-i)
                x-=nums[i]
                i+=1
            
            elif x<target and j<l:
                x+=nums[j]
                j+=1
            else:
                x-=nums[i]
                i+=1
        
        return ans if flag else 0
