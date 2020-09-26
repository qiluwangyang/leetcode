from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        Counter(nums).most_common(1)