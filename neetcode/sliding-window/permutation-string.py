class Solution:
    """
        This Works, but has a time poor time/space complexity
        O(m * n log n)
        n = len(s1), m = len(s2)

        Expected: O(n) where n = max(len(s1), len(s2))
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        s1 = "".join(sorted(s1))
        while r <= len(s2):
            if "".join(sorted(s2[l:r])) == s1:
                return True

            l, r = l + 1, r + 1
        return False

strings = [
    ["abc", "lecabee", True],
    ["abc", "leabcee", True],
    ["abc", "lecaabee", False],
    ["abc", "lecaebe", False],
    ["hello", "ooolleoooleh", False],
]

solution = Solution()
for s1, s2, e in strings:
    r = solution.checkInclusion(s1, s2)
    error = "ERROR " if r != e else "PASSED"
    print("{} s1: {}, s2 {} Result: {}, Expected: {}".format(error, s1, s2, r, e))