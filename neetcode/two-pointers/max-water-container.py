from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        maxArea = 0
        while l < r:
            b = r - l
            h = min(heights[l], heights[r])
            a = b * h

            if a > maxArea: maxArea = a

            if heights[l] > heights[r]: r -= 1
            else: l += 1

        return maxArea

s = Solution()
heights = [1, 7, 2, 5, 4, 7, 3, 6]
print("Input: ", heights, "Result:", s.maxArea(heights), "Expected: 36")

heights = [2, 2, 2]
print("Input: ", heights, "Result:", s.maxArea(heights), "Expected: 4")

heights=[1,8,100,2,100,4,8,3,7]
print("Input: ", heights, "Result:", s.maxArea(heights), "Expected: 200")

