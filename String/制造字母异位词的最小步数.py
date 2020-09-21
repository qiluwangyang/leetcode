class Solution:
    @staticmethod
    def minSteps(des: str, src: str) -> int:
        # 使用counter解决，另外可以使用数组计数的方式解决
        count = 0
        from collections import Counter
        s_num = Counter(des)
        t_num = Counter(src)
        for key in s_num.keys():
            if s_num[key] - t_num[key] > 0:
                count += s_num[key] - t_num[key]
        return count
