class Solution:
    @staticmethod
    def subtractProductAndSum(n: int) -> int:
        multi = 1
        count = 0
        while n:
            multi *= (n % 10)
            count += (n % 10)
            n //= 10

        return multi - count


solution = Solution()
print(solution.subtractProductAndSum(4421))
