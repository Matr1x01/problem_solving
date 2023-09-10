class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        memory = dict()
        memory['to-1'] = 1
        memory['from'+str(l)] = 1
        product = 1
        for i, v in enumerate(nums):
            product *= v
            memory['to'+str(i)] = product

        product = 1
        for i, v in enumerate(nums[::-1]):
            product *= v
            memory['from'+str(l-i-1)] = product

        return [memory['to'+str(i-1)]*memory['from'+str(i+1)] for i in range(l)]
