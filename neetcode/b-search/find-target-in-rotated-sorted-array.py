from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b, e, l = 0, len(nums) - 1, len(nums)
        while b <= e:
            m = b + (e - b) // 2
            if m + 1 == l or nums[m] < nums[m - 1]:
                break
            if nums[m] > nums[m + 1]:
                m += 1
                break

            if nums[m] > nums[b]: b = m + 1; continue
            if nums[m] < nums[b]: e = m - 1; continue
            break
        r = self.binarySearch(nums[0:m], target)

        if r is None:
            r = self.binarySearch(nums[m:l], target, m)
        return r if r is not None else -1

    def binarySearch(self, nums: List[int], target: int, incr: int = 0) -> int | None:
        b, e = 0, len(nums) - 1
        while b <= e:
            m = b + (e - b) // 2
            if nums[m] == target: return m + incr
            if nums[m] > target: e = m - 1
            if nums[m] < target: b = m + 1
        return None

inputs = [
    [[3, 1], 1, 1],
    [[1], 0, -1],
    [[3,4,5,6,1,2], 1, 4],
    [[3,5,6,0,1,2], 4, -1],
    [[4,5,6,7,8,9], 6, 2],
    [[4,5,6,7,8,9], 10, -1],
    [[9,8,4,5,6,7], 9, 0],
    [[9,8,4,5,6,7], 10, -1],
    [[11,13,15,17], 13, 1],
]

s = Solution()
for nums, t, e in inputs:
    r = s.search(nums, t)
    err = "PASSED" if r == e else "ERROR"
    print("{} In nums: {}, found t = {} in {} pos. Expected: {}".format(err, nums, t, r, e))
