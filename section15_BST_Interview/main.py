# BST: Interview / LeetCode Exercises Location
# Practically all LeetCode BST exercises require recursion, which will be covered later in the course in the following sections:



# Recursive Binary Search Trees: Dive deep into how recursion powers the core operations in BSTs, such as searching, insertion, and deletion. We'll start with the basics and gradually move to more complex applications.

# Tree Traversal: Learn the various ways to navigate through a tree, a skill essential for understanding and manipulating BSTs. This section will cover:

# Breadth-First Search (BFS)

# Depth First Search (DFS) in three variants:

# Pre-Order

# In-Order

# Post-Order


# LeetCode / Interview Questions We Will Cover:

# To ensure you're well-prepared for technical interviews, we'll tackle some of the most common BST interview questions, including:

# Deleting a Node from a BST: Understand the strategies to remove a node while maintaining the BST properties.

# Converting a Sorted List to a Balanced BST: Learn how to transform a sorted array or list into a balanced BST to ensure operations are efficient.

# Inverting a BST: Explore the concept of flipping a BST to mirror its structure.

# Validating a BST: Discover how to check if a binary tree satisfies BST conditions, an essential problem-solving skill.

# By the end of these sections, you'll have a solid foundation in both recursion and BSTs.


# Deleting a Node from a BST: Understand the strategies to remove a node while maintaining the BST properties.
def deleteNode(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root

# Converting a Sorted List to a Balanced BST: Learn how to transform a sorted array or list into a balanced BST to ensure operations are efficient.
def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])

    return node

# Converting a Sorted List to a Balanced BST: Learn how to transform a sorted array or list into a balanced BST to ensure operations are efficient.
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

# Validating a BST: Discover how to check if a binary tree satisfies BST conditions, an essential problem-solving skill.
def isValidBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (isValidBST(root.left, low, root.val) and
            isValidBST(root.right, root.val, high))

# Helper function to find the node with the minimum value in a BST
def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Example usage:
if __name__ == "__main__":
    # Create a sample BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # Delete a node
    root = deleteNode(root, 3)

    # Convert sorted array to BST
    sorted_nums = [1, 2, 3, 4, 5, 6, 7]
    bst_root = sortedArrayToBST(sorted_nums)

    # Invert the BST
    inverted_root = invertTree(bst_root)

    # Validate the BST
    is_bst = isValidBST(bst_root)
    print("Is valid BST:", is_bst)