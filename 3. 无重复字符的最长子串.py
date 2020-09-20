class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        tmp = res = ''
        for i in s:
            if i not in tmp:
                tmp += i
            else:
                # 当测试用例类似为aaaa时，tmp.index(i) + 1会索引越界
                # 所以需要进行分片，分片超过索引时返回为空
                tmp = tmp[tmp.index(i) + 1:]
                tmp += i
            if len(res) < len(tmp):
                res = tmp
        return len(res)
