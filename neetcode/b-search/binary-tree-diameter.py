from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l = self.maxDepth(root)
        while root.left is not None:
            l = max(l, self.maxDepth(root.left))
            root.left = root.left.left

        r = self.maxDepth(root)
        while root.right is not None:
            r = max(l, self.maxDepth(root.right))
            root.right = root.right.right

        return max(l, r)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def printTree(self, root, level = 0, prefix= "Root: "):
        if root is None: return

        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            self.printTree(root.left, level + 1, "Left: ")
            self.printTree(root.right, level + 1, "Right: ")

inputs = [
    [TreeNode(1, TreeNode(2), TreeNode(3)), 2],
    [TreeNode(1, None, TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4))), 4],
]

s = Solution()
for root, expected in inputs:
    s.printTree(root)
    print("Expected: {} Result: {}\n\n".format(expected, s.diameterOfBinaryTree(root)))