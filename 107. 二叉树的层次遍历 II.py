"""给定一个二叉树，返回其节点值自底向上的层次遍历。
即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历,例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        tree_res, level = [], 0
        if not root:
            return []
        tree_res.append([root])
        while level < len(tree_res):
            level_res = []
            for tree in tree_res[0]:
                if tree.left:
                    level_res.append(tree.left)
                if tree.right:
                    level_res.append(tree.right)
            if level_res:
                tree_res = [level_res] + tree_res
            level += 1
        res = []
        for level in tree_res:
            level_val = []
            for tree in level:
                level_val.append(tree.val)
            res.append(level_val)

        return res


sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.levelOrderBottom(root))
