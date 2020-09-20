"""
给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""
from typing import List


class Solution:
    # 相同元素索引取第一个，部分用例不通过
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums[1:]:
                if i + j == target:
                    return [nums.index(i), nums.index(j)]

    # 完善
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1 + i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # hash解决,存在唯一解
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, ele in enumerate(nums):
            if target - ele in d:
                return [d[ele], idx]
            d[ele] = idx



nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum3(nums, target))