class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls, rs = 0, sum(nums)
        for i, val in enumerate(nums):
            ls += val
            if ls == rs:
                return i
            rs -= val
        return -1
