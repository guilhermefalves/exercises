from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        l, pairs = len(nums), []
        for i in range(l):
            num = nums[i]
            if i > 0 and num == nums[i - 1]:
                continue

            start, end = i + 1, l - 1
            while start < end:
                sum = nums[start] + num + nums[end]
                if sum < 0:
                    start += 1
                    continue

                if sum > 0:
                    end -= 1
                    continue

                pairs.append([num, nums[start], nums[end]])
                end -= 1
                start += 1
                while nums[start] == nums[start - 1] and start < end:
                    start += 1

        return pairs

s = Solution()

print("Result:", s.threeSum([-1, 0, 1, 2, -1, -4]), "Expected:", [[-1, -1, 2], [-1, 0, 1]])
print("Result:", s.threeSum([[0, 1, 1]]), "Expected:", [])
print("Result:", s.threeSum([[-2, 0, 0, 2, 2]]), "Expected:", [[-2, 0, 2]])