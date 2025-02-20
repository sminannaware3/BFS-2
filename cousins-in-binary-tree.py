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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_level = -1
        y_level = -1
        x_parent = -1
        y_parent = -1
        # BFS
        dq = deque()
        dq.append(root)
        level = 0
        while len(dq) > 0:
            size = len(dq)
            for i in range(size):
                curr = dq.popleft()
                if (curr.left != None and curr.left.val == x) or (curr.right != None and curr.right.val == x): 
                    x_level = level+1
                    x_parent = curr.val
                if (curr.left != None and curr.left.val == y) or (curr.right != None and curr.right.val == y): 
                    y_level = level+1
                    y_parent = curr.val
                if curr.left != None: dq.append(curr.left)
                if curr.right != None: dq.append(curr.right)
            if x_level != -1 or y_level != -1: break    
            level += 1
        if x_level > -1 and y_level > -1 and x_level == y_level and x_parent != y_parent:
            return True
        else: return False


# Time O(n)
# Space O(h) hight of recursion
class Solution:
    def __init__(self):
        self.x_level = -1
        self.y_level = -1
        self.x_parent = -1
        self.y_parent = -1

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # DFS
        self.dfs(root, x, y, 0)
        return self.x_level > -1 and self.y_level > -1 and self.x_level == self.y_level and self.x_parent != self.y_parent
    
    def dfs(self, root: Optional[TreeNode], x: int, y: int, level: int) -> None:
        if root == None: return
        if root.left != None and root.left.val == x or root.right != None and root.right.val == x:
            self.x_level = level+1
            self.x_parent = root.val
        if root.left != None and root.left.val == y or root.right != None and root.right.val == y:
            self.y_level = level+1
            self.y_parent = root.val
        
        self.dfs(root.left, x, y, level + 1)
        self.dfs(root.right, x, y, level + 1)