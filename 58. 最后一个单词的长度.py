class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.strip().split(' ')
        return len(tmp[-1])
solu = Solution()
print(solu.lengthOfLastWord('a'))