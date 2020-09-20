class Solution:
    def mySqrt(self, x: int) -> int:
        tmp = x // 2
        while True:
            if tmp * tmp > x:
                tmp //= 2
                continue
            else:
                return tmp
solu = Solution()
print(solu.mySqrt(10))