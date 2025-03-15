from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before, after = [1] * n, [1] * n

        for i in range(1, n):
            before[i] = nums[i-1] * before[i-1]

        for i in range(n - 2, -1, -1):
            after[i] = nums[i + 1] * after[i + 1]

        for i in range(n):
            nums[i] = after[i] * before[i]

        return nums
s = Solution()

print(s.productExceptSelf([1, 2, 3, 4]))
print("Expected: ", [24, 12, 8, 6])

print(s.productExceptSelf([-1, 0, 1, 2, 3]))
print("Expected: ", [0, -6, 0, 0, 0])

print(s.productExceptSelf([1, 2, 4, 6]))
print("Expected: ", [48, 24, 12, 8])

# Input    = [1, 2, 3, 4]
# Before   = [1, 1, 2, 6]
# After    = [24, 12, 4, 1]
# Expected = [24, 12, 8, 6]
