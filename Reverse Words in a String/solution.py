class Solution:
    def reverseWords(self, s: str) -> str:
        s = " "+s
        l = len(s)-1
        i, j = l, l
        ans = []
        while True:
            if i == -1:
                break
            if s[i] == " ":
                x = s[i+1:j+1]
                if x != '' and x != ' ':
                    ans.append(x)
                j = i-1
            i -= 1
        print(ans)
        return(" ".join(ans))
