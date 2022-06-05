# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path' \
#              ' from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, visited=False):
        self.val = val
        self.left = left
        self.right = right

# Iterative BFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            visited = []
            for item in level:
                if item.left:
                    visited.append(item.left)
                if item.right:
                    visited.append(item.right)
            level = visited
        return depth

# Recursive DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        return dfs(root, 0)
