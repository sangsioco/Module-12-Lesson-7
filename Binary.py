class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# In-order

def in_order_traversal(root):
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    
    traverse(root)
    return result

# Pre-order
def pre_order_traversal(root):
    result = []
    
    def traverse(node):
        if node:
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)
    
    traverse(root)
    return result

# Post-order
def post_order_traversal(root):
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
    
    traverse(root)
    return result

# Testing
# Create the binary tree
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(40)
root.left.right = TreeNode(20)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

# Test the traversal algorithms
print("In-order Traversal:", in_order_traversal(root))
print("Pre-order Traversal:", pre_order_traversal(root))
print("Post-order Traversal:", post_order_traversal(root))
