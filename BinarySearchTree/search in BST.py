class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

            else:
                # Duplicate values are ignored
                return

    def search(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True

            elif value < current.value:
                current = current.left

            else:
                current = current.right

        return False

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)


# Create BST
tree = BST()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.insert(value)

# Inorder traversal
tree.inorder(tree.root)

# Search
print("\nFound:", tree.search(40))
print("Found:", tree.search(100))