from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = len(nums)
        if l == 0:
            return 0

        aux, longest = 1, 1
        for i in range(0, l - 1):
            curr, next = nums[i], nums[i + 1]
            if curr == next:
                continue

            if curr + 1 != next:
                aux = 1
                continue

            aux += 1
            if aux >= longest:
                longest = aux

        return longest

s = Solution()
nums = [2, 20, 4, 10, 3, 4, 5]
print("Result:: ", s.longestConsecutive(nums), "Expected:: 4")

nums = [0,3,2,5,4,6,1,1]
print("Result:: ", s.longestConsecutive(nums), "Expected:: 7")