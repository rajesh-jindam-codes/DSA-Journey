from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

def rightView(node):
    if not node:
        return 
    queue=deque()
    result=[]
    queue.append(node)
    while queue:
        levelSize=len(queue)
        for i in range(levelSize):
            node=queue.popleft()
            if i==levelSize-1:
                e=result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
print(rightView(root))