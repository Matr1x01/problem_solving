class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = len(nums)
        i = 0
        while True:
            if i >= j:
                break
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(j, 0)
                j -= 1
            else:
                i += 1
