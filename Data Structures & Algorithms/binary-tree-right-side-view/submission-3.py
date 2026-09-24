# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not root:
            return res
        
        queue = deque()
        queue.append(root)
        while len(queue) >0:
            right_most = None
            for i in range (len(queue)):
                curr = queue.popleft()
                right_most = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(right_most)
        return res
                
            
