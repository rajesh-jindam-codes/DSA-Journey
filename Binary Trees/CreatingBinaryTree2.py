from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildTree(values):
    if not values or values[0] is None:
        return None
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    while queue and i<len(values):
        curr=queue.popleft()
        if values[i] is not None:
            curr.left=TreeNode(values[i])
            queue.append(curr.left)
        i+=1
        if i<len(values) and values[i] is not None:
            curr.right=TreeNode(values[i])
            queue.append(curr.right)
        i+=1
    return root
values = [1, 2, 3, 4, 5, None, 7]
root = buildTree(values)
print(root.val)               # 1
print(root.left.val)          # 2
print(root.right.val)         # 3
print(root.left.left.val)     # 4
