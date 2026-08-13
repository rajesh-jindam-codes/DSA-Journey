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
class Solution:
    def connect(self,root):
        if not root:
            return None
        queue=deque([root])
        while queue:
            levelSize=len(queue)
            prev=None
            for _ in range(levelSize):
                node=queue.popleft()
                if prev:
                    prev.next=node
                prev=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
obj=Solution()
print(obj.connect(root))