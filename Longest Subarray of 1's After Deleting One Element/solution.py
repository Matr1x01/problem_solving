class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        l = len(chars)
        chars.append(' ')
        count = 1
        while True:
            if i == l:
                break
            if chars[i] == chars[i+1]:
                count += 1
                chars.pop(i+1)
                l -= 1
            else:
                if count > 1:
                    c = list(str(count))
                    for j, x in enumerate(c):
                        chars.insert(i+j+1, x)
                    l += len(c)
                    i += (len(c))

                count = 1
                i += 1

        chars.pop()
        return len(chars)
