class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        mx = '2147483647'

        if x < 0:
            neg = True
            mx = '2147483648'
            x *= -1

        numStr = str(x)
        sz = len(numStr)

        if (sz < 10 or numStr[-1] == '0'):
            return int(numStr[::-1])*(-1 if neg else 1)

        flag = True

        for i in range(10):
            if int(mx[i]) > int(numStr[sz-i-1]):
                flag = True
                break
            if int(mx[i]) < int(numStr[sz-i-1]):
                flag = False
                break

        return int(numStr[::-1])*(-1 if neg else 1) if flag else 0
