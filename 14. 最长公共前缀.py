from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        for ele in strs:
            if not ele:
                return common
        length = len(strs[0])
        if strs[0][0] != strs[1][0]:
            return common
        for i in range(length):
            common = strs[0][:i+1]
            for j in range(len(strs)):
                if common == strs[j][i]:
                    continue
                else:
                    return common


solu = Solution()
print(solu.longestCommonPrefix(["dog","racecar","car"]))