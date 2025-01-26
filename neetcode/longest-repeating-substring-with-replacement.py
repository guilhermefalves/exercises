class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        f, l, longest, curr = 0, 0, 0, 0
        for r in range(len(s)):
            letters[s[r]] = letters.get(s[r], 0) + 1

            f = max(f, letters[s[r]])
            if (r - l + 1) - f > k:
                letters[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

strings = [
    ["XYYX", 1, 3],
    ["XYYX", 2, 4],
    ["AAABABB", 1, 5],
    ["AABABBA", 1, 4],
    ["ABBB", 2, 4],
]
solution = Solution()
for s, k, e in strings:
    r = solution.characterReplacement(s, k)
    error = "ERROR " if r != e else "PASSED"
    print("{} s: {}, k {} Result: {}, Expected: {}".format(error, s, k, r, e))