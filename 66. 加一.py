"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for ele in digits:
            res += str(ele)
        res = str(int(res) + 1)
        a = [ele for ele in map(int, list(res))]
        return a


