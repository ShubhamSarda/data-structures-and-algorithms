class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self, start, traversal):
        # Root -> Left -> Right
        if start is None:
            return
        
        traversal.append(start.value)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)

        return traversal

    def inorder(self, start, traversal):
        # Left -> Root -> Right
        if start is None:
            return
        
        self.inorder(start.left, traversal)
        traversal.append(start.value)
        self.inorder(start.right, traversal)

        return traversal

    def postorder(self, start, traversal):
        # Left -> Right -> Root
        if start is None:
            return
        
        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.value)

        return traversal

tree = BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.preorder(tree.root, []))
print(tree.inorder(tree.root, []))
print(tree.postorder(tree.root, []))