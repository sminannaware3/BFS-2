# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(n)
# Space O(n)
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        result = []
        if root == None: return result
        dq = deque() #FIFO
        dq.append(root)
        level = 0
        while len(dq) > 0:
            size = len(dq)
            while size > 0:
                curr = dq.popleft()
                if len(result) == level+1: result[level] = curr.val
                else: result.append(curr.val)
                if curr.left != None: dq.append(curr.left)
                if curr.right != None: dq.append(curr.right)
                size -= 1
            level += 1
        return result
    
# Time O(n)
# Space O(h) depth of recursion
class Solution:
    def __init__(self):
        self.result = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #DFS     
        if root == None: return self.result
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root: Optional[TreeNode], level: int) -> None:
        if root == None: return
        if len(self.result) < level + 1: self.result.append(root.val)

        self.dfs(root.right, level + 1)
        self.dfs(root.left, level + 1)