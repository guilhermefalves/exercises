from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        b, e = 0, l - 1
        while b <= e:
            m = b + (e - b) // 2
            if m + 1 == l or nums[m] < nums[m - 1]: break
            if nums[m] > nums[m + 1]: m += 1; break

            if nums[m] > nums[b]: b = m + 1; continue
            if nums[m] < nums[b]: e = m - 1; continue
            break

        return min(nums[0], nums[m])

inputs = [
    [[3, 1], 1],
    [[1], 1],
    [[11,13,15,17], 11],
    [[3,4,5,6,1,2], 1],
    [[3,5,6,0,1,2], 0],
    [[4,5,6,7,8,9], 4],
    [[4,5,6,7,8,9], 4],
    [[9,8,4,5,6,7], 4],
]

s = Solution()
for nums, e in inputs:
    r = s.findMin(nums)
    err = "PASSED" if r == e else "ERROR "
    print("{} In nums: {}, the min is: {}. Expected: {}".format(err, nums, r, e))
