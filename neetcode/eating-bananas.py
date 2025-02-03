import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, p = 1, max(piles)
        while i <= p:
            m = i + (p - i) // 2
            t = self.timeToEat(piles, m)
            # print("TESTING WITH >> m = {}, resulted in t = {}".format(m, t))
            if t <= h:
                r = m
                p = m - 1
                continue
            i = m + 1
        return r

    def timeToEat(self, piles: List[int], v: int) -> int:
        t = 0
        for p in piles:
            t += math.ceil(p / v)
        return t

inputs = [
    [[1,4,3,2], 9, 2],
    [[25,10,23,4], 4, 25],
    [[3,6,7,11], 8, 4],
]

s = Solution()
for piles, h, e in inputs:
    r = s.minEatingSpeed(piles, h)
    err = "PASSED" if r == e else "ERROR"
    # print("TIME TO EAT {} WITH VELOCITY 1 IS {}".format(piles, s.timeToEat(piles, 1)))
    # print("TIME TO EAT {} WITH VELOCITY 2 IS {}".format(piles, s.timeToEat(piles, 2)))
    # print("TIME TO EAT {} WITH VELOCITY 3 IS {}".format(piles, s.timeToEat(piles, 3)))
    # print("TIME TO EAT {} WITH VELOCITY 4 IS {}".format(piles, s.timeToEat(piles, 4)))
    # print("TIME TO EAT {} WITH VELOCITY 5 IS {}".format(piles, s.timeToEat(piles, 4)))
    print("{} Piles: {}, h: {} - result: {} expected: {}".format(err, piles, h, r, e))

# h = number of hours you have to eat all the bananas