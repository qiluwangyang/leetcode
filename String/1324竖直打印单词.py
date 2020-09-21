from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(ele) for ele in words)
        res = [[] * max_length]
        for word in words:
            for i in range(max_length):
                if i < len(word):
                    res[i].append(word[i])
                else:
                    res[i].append(' ')
        return res

solu = Solution()
print(solu.printVertically('to be or not to be'))
