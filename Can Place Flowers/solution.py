class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        x = 0
        i = 1
        while i < len(flowerbed)-1:
            if flowerbed[i-1:i+2] == [0, 0, 0]:
                x += 1
                i += 1

            i += 1

        return x >= n
