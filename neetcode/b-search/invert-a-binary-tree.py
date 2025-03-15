from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    def printTree(self, root, level = 0, prefix= "Root: "):
        if root is None: return

        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            self.printTree(root.left, level + 1, "Left: ")
            self.printTree(root.right, level + 1, "Right: ")

inputs = [
    [TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(2))],
    [TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),
        TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(4)), TreeNode(2, TreeNode(7), TreeNode(6)))
    ],
]

s = Solution()
for root, expected in inputs:
    print("\nInput:")
    s.printTree(root)

    print("\nExpected:")
    s.printTree(expected)

    print("\nOutput:")
    output = s.invertTree(root)
    s.printTree(output)
    print("-----------------\n\n")