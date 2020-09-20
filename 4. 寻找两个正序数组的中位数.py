from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums = sorted(nums1)
        if len(nums) % 2 == 1:
            return float(nums[len(nums)//2])
        elif len(nums) % 2 == 0:
            return float((nums[len(nums)//2] + nums[len(nums)//2 - 1])/2)

solu = Solution()
l1 = [1, 3]
l2 = [2]
print(solu.findMedianSortedArrays(l1, l2))
