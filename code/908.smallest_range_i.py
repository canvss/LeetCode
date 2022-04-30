# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/30 11:03
from typing import List


class Solution:
    def smallestRangeI(nums: List[int], k: int) -> int:
        return max(0, max(nums) -min(nums) -2*k)


res = Solution.smallestRangeI(nums=[0,10], k=2)
res2 = Solution.smallestRangeI(nums=[1,5,4,7,6], k=2)
print(res2)

