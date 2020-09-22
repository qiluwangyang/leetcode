from typing import List


class Solution:
    @staticmethod
    def permutation(s: str) -> List[str]:
        res = []
        if s == '':
            return res

        def helper(tmp, path):
            """
            :param tmp:存放去除一个元素的字符串
            :param path: 存放加入字符的临时字符串
            :return: None
            """
            if tmp == '':
                res.append(path)
                return
            for i in range(len(tmp)):
                helper(tmp[:i] + tmp[i+1:], path + tmp[i])

        helper(s, '')
        return res
