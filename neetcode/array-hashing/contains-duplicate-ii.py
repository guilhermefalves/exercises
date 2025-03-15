from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for i in range(len(nums)):
            j = h.get(nums[i])
            # print(f"i={i} j={j} numms[i]={nums[i]} h={h}")
            if j is not None and abs(i - j) <= k:
                return True
            h.update({nums[i]: i})
        return False

expected = [
    [[1,2,3,1], 3, True],
    [[1,0,1,1], 1, True],
    [[1,2,3,1,2,3], 2, False],
]

s = Solution()
for nums, k, e in expected:
    r = s.containsNearbyDuplicate(nums, k)
    print(f"Nums = {nums}\n   k = {k}, Result: {r} Expected: {e}\n")
