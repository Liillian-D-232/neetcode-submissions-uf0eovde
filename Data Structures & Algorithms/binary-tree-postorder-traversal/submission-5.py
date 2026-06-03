# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rec_post(root):
            if not root:
                return
          
            left = rec_post(root.left)
            right = rec_post(root.right)
            cur = root.val
            res.append(cur)

        rec_post(root)
        return res
