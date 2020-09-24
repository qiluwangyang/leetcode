class Solution:
    @staticmethod
    def getPermutation(n: int, k: int) -> str:
        # 暴力回溯超时，需要优化
        res = []
        src_lst = [str(ele) for ele in range(1, n+1)]

        def helper(decrease_lst, increase_lst):
            if not decrease_lst:
                res.append(increase_lst)

            for i in range(len(decrease_lst)):
                helper(decrease_lst[:i] + decrease_lst[i+1:], increase_lst + [decrease_lst[i]])
        helper(src_lst, [])
        return ''.join(res[k-1])


solution = Solution()
print(solution.getPermutation(4, 9))
