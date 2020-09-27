from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, i: int, j: int) -> int:
        return sum(self.nums[i: j+1])
