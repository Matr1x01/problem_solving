class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1Len = len(str1)
        str2Len = len(str2)

        return (str1[:gcd(str1Len, str2Len)]) if str1+str2 == str2+str1 else ""
