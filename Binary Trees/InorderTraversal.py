class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
drinks=Node('drinks')
hot=Node('hot')
cold=Node('cold')
tea=Node('tea')
coffe=Node('coffe')
cola=Node('cola')
sprite=Node('sprite')
drinks.left=hot
drinks.right=cold
hot.left=tea
hot.right=coffe
cold.left=cola
cold.right=sprite

def inorderTraversal(node):
    if not node:
        return
    
    inorderTraversal(node.left)
    print(node.val)
    inorderTraversal(node.right)
inorderTraversal(drinks)

print(hot.left.val)