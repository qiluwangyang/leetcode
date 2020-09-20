from typing import List


class Solution:
    # 迭代方法求解子集
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums:
            subset += [[num] + ele for ele in subset]
        return subset
