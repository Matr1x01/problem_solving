class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m, x = 0, 0
        for i in gain+[0]:
            m = max(m, x)
            x += i
        return m
