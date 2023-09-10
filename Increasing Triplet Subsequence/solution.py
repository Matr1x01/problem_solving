class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstMin = float('inf')
        secoundMin = float('inf')

        for i in nums:
            if firstMin >= i:
                firstMin = i
            elif secoundMin >= i:
                secoundMin = i
            else:
                return True

        return False
