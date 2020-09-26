from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 最初判断最小公倍数，还得判断是否所有元素相等，数组长度是否为1等问题
        # 思路应该为最小值需要增加多少次与次小值相等，直至所有元素相等，即数组总和-最小值*数组长度
        return sum(nums) - min(nums) * len(nums)


solution = Solution()
print(solution.minMoves([1, 1, 1]))
