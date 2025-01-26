class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        letters, longest = {}, 0
        while r < len(s):
            if letters.get(s[r]) is not None and letters.get(s[r]) >= l:
                l = letters.get(s[r]) + 1

            letters.update({s[r]: r})
            r += 1
            longest = max(longest, r - l)
        return longest


strings = [
    ["abcc", 3],
    ["zxyzxyz", 3],
    ["xxxx", 1],
    ["pwwkew", 3],
    ["dvdf", 3],
    ["abcabcbb", 3],
    [" ", 1],
    ["", 0],
    ["au", 2],
    ["abba", 2],
]
solution = Solution()
for s, e in strings:
    r = solution.lengthOfLongestSubstring(s)
    error = 'ERROR' if r != e else 'PASSED'
    print("s: {}, Result: {}, Expected: {} {}".format(s, r, e, error))