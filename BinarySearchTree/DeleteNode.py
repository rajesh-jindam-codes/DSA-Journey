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
    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.value==key:
            return self.deletion(root)
        temp=root
        while temp is not None:
            if temp.value>key:
                if temp.left is not None and temp.left.value==key:
                    temp.left=self.deletion(temp.left)
                    break
                else:
                    temp=temp.left
            else:
                if temp.right is not None and temp.right.value==key:
                    temp.right=self.deletion(temp.right)
                    break
                else:
                    temp=temp.right
        return root
    def deletion(self,node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            rightChild=node.right
            lastRight=self.findLastRight(node.left)
            lastRight.right=rightChild
            return node.left
    def findLastRight(self,node):
        while node.right is not None:
            node=node.right
        return node


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
print(tree.deleteNode(tree.root,30))