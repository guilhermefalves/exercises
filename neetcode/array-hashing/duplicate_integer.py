# from sortedcontainers import SortedList
from typing import List


class Solution:
    """
        https://neetcode.io/problems/duplicate-integer
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashes = {}
        for n in nums:
            hashes.update({n: hashes.get(n, 0) + 1})
            if hashes[n] > 1:
                return True

        return False


nums = [1, 2, 3, 3]

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))
print(solution.hasDuplicate([1, 2, 3]))
print(solution.hasDuplicate([3, 3, 1, 2]))
