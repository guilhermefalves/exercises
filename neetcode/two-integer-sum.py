from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - nums[i]
            if diff in numsHash:
                return [numsHash[diff], i]
            
            numsHash[curr] = i

s = Solution()
print(s.twoSum([3, 4, 5, 6], 7))
print(s.twoSum([4, 5, 6], 10))
print(s.twoSum([5, 5], 10))
print(s.twoSum([3, 2, 3], 6))