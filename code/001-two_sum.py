# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/30 12:37
from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        li = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    li.append(i)
                    li.append(j)
                    return li


res = Solution.twoSum([9,4,3,1,2,7], 11)
print(res)