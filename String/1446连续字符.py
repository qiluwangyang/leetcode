class Solution:
    @staticmethod
    def maxPower(s: str) -> int:
        max_count = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                if max_count < count:
                    max_count = count
                count = 1
        return max_count

    @staticmethod
    def fun1(s1: str) -> int:
        # 双指针
        res = 1
        left, right = 0, 1
        while right < len(s1):
            if s1[right] != s1[left]:
                res = max(right - left, res)
                left = right
            right += 1
        return max(right - left, res)

    @staticmethod
    def fun2(s2: str) -> int:
        # 字符串预处理
        res = max_count = 1
        s2 += '🐕'
        for i in range(len(s2)):
            if s2[i] == s2[i-1]:
                res += 1
            else:
                max_count = max(max_count, res)
                res = 1
        return max_count

    @staticmethod
    def fun3(s3: str) -> int:
        # 使用正则贪婪匹配
        # \w: 匹配字符
        # (\w): 捕获组
        # \1*: 引用捕获组1,匹配{0, inf}次
        import re
        return max(map(lambda x: len(x.group()), re.finditer(r"(\w)\1*", s3)))

    @staticmethod
    def fun4(s4: str) -> int:
        # 有序统计groupby,无序统计使用counter
        from itertools import groupby
        return max(len(list(group)) for _, group in groupby(s4))
