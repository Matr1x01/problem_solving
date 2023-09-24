class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x=set(nums)
        count=0
        ans=0
        for i in x:
            y=int(i)-1
            if y not in x:
                j=i
                while j in x:
                    count+=1
                    j+=1
                ans=max(ans,count)
                count=0
        return ans
                