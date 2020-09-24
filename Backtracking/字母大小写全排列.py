from typing import List


class Solution:
    @staticmethod
    def letterCasePermutation(s: str) -> List[str]:
        res = []

        def helper(src_str, tmp_str):
            for i in range(len(src_str)):
                if 97 <= ord(src_str[i]) <= 122:
                    helper(src_str[i+1:], tmp_str + src_str[i].capitalize())
                    helper(src_str[i+1:], tmp_str + src_str[i])
                elif 65 <= ord(src_str[i]) <= 90:
                    helper(src_str[i+1:], tmp_str + src_str[i].lower())
                    helper(src_str[i+1:], tmp_str + src_str[i])
                else:
                    tmp_str += src_str[i]
                    continue
            if tmp_str and len(tmp_str) == len(s):
                res.append(tmp_str)
        helper(s, '')
        return res


solution = Solution()
print(solution.letterCasePermutation('12345'))
