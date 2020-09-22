# leetcode
leetcode刷题记录
##1 算法
###1 回溯算法
1.画递归树，找到状态变量
2.确定结束条件
3.找准选择列表
4.判断是否剪枝
5.做出选择，递归调用，进入下一层
6.撤销选择

##2 技巧
1.有序统计和无序统计
    
    有序统计：itertools.groupby    
    无序统计：collections.Counter
2.正则表达式

    匹配英文字符：\w
    捕获组：(\w)
    引用捕获组1：\1
3.短路运算符

    某些情况下可以代替if else条件判断语句，例如累加时不使用if条件判断语句
    ```
    class Solution:
        def sumNums(self, n: int) -> int:
            return n > 0 and n + self.sumNums(n-1)  
    ```

4.元素累计
    
    reduce()函数
