class Solution:
    @staticmethod
    def numTilePossibilities(tiles: str) -> int:
        """
        :param tiles: 给定字符串
        :return: 返回可以打印的非空字母序列的数目
        """
        res = []

        def helper(cur_lst, tmp):
            """
            :param cur_lst: 存放列表剩余元素
            :param tmp: 存放加入到临时列表的元素
            :return: None
            """
            if tmp:
                res.append(tmp)
            for i in range(len(cur_lst)):
                # 剪枝,当所取元素已经在列表中，continue到下一次循环，不能使用return
                if cur_lst[i] in cur_lst[:i]:
                    continue
                helper(cur_lst[:i] + cur_lst[i+1:], tmp + [cur_lst[i]])
        helper(tiles, [])
        return len(res)


solution = Solution()
print(solution.numTilePossibilities('AAB'))
