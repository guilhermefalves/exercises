from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b, e = 0, len(matrix) - 1
        while b <= e:
            m = b + (e - b) // 2
            if matrix[m][0] == target: return True

            if matrix[m][0] <= target <= matrix[m][len(matrix[m]) - 1]:
                return self.binarySearch(matrix[m], target)

            if matrix[m][0] > target: e = m - 1
            if matrix[m][0] < target: b = m + 1
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        b, e = 0, len(nums) - 1
        while b <= e:
            m = b + (e - b) // 2
            if nums[m] == target: return True
            if nums[m] > target: e = m - 1
            if nums[m] < target: b = m + 1
        return False

inputs = [
    [[[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30, True],
    [[[1,3]], 3, True],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True],
    [[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10, True],
    [[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15, False],

]

s = Solution()
for nums, target, e in inputs:
    r = s.searchMatrix(nums, target)
    err = "PASSED" if r == e else "ERROR"
    print("Nums: {}, target: {}, result: {} {} expected: {}".format(nums, target, r, err, e))