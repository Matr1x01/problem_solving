class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 1
        x = sum(nums[0:k])
        m = x/k
        while i+k <= len(nums):
            x = x-nums[i-1]+nums[i+k-1]
            m = max(m, x/k)
            i += 1
        return m
