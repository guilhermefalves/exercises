from typing import List
class Solution:
    """
        This Works, but has a time poor time complexity
        O(m * log n) Expected: O(log (n * m)) where n = max(len(s1), len(s2))
        where m = rows and n is the columns of the matrix
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            if self.binarySearch(nums, target):
                return True
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        b, e = 0, len(nums) - 1
        while b <= e:
            m = b + (e - b) // 2
            if nums[m] == target:
                return True
            if nums[m] > target:
                e = m - 1
            if nums[m] < target:
                b = m + 1
        return False

inputs = [
    [[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10, True],
    [[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15, False],
]

s = Solution()
for nums, target, e in inputs:
    r = s.searchMatrix(nums, target)
    err = "PASSED" if r == e else "ERROR"
    print("Nums: {}, target: {}, result: {} {} expected: {}".format(nums, target, r, err, e))