from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = begin + (end - begin) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                begin = mid + 1
            if target < nums[mid]:
                end = mid -1
        return -1

inputs = [
    [[-1,0,2,4,6,8], 4, 3],
    [[-1,0,2,4,6,8], 3, -1],
]

s = Solution()
for nums, target, e in inputs:
    r = s.search(nums, target)
    err = "PASSED" if r == e else "ERROR"
    print("Nums: {}, target: {}, result: {} {} expected: {}".format(nums, target, r, err, e))
