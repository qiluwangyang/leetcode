# leetcode
leetcode刷题记录

##2 技巧
1.有序统计和无序统计
    
    有序统计：itertools.groupby    
    无序统计：collections.Counter
        Counter继承dict类，所以也可以使用Counter(iterable).get(ele, default)
        Counter(iterable).most_common(1)返回计数最多的键值对元组列表，类似于[('a', 2)]
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

5.删除列表元素可以考虑使用del，比remove函数耗时少
6.set()函数返回的是set类，如果还要使用原先类型需要再次转换
7.enumerate()函数可以指定初始值，enumerate(iterable, start=init_num)，返回的第一个值为索引，第二个值为可迭代的元素
8.位运算
    按位与：
    按位或：
    按位异或：
    按位取反：
