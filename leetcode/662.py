# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = Deque([(root, 1)])
        max_width = 0
        while q:
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                current_node, node_position = q.popleft()
                if current_node.left:
                    q.append((current_node.left, node_position * 2 - 1))
                if current_node.right:
                    q.append((current_node.right, node_position * 2))
        return max_width