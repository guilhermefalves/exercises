import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())

        j = len(s)
        for i in range(j):
            j -= 1
            if (s[i] != s[j]):
                return False

        return True


# s = Solution()
# print(s.isPalindrome("Was it a car or a cat I saw?"))

s = Solution()
print(s.isPalindrome("tab a cat"))
