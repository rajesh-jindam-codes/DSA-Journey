from collections import deque
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

def levelTraversal(node):
    result=[]
    queue=deque([])
    queue.append(node)
    while len(queue)!=0:
        e=queue.popleft()
        result.append(e.val)
        if e.left:
            queue.append(e.left)
        if e.right:
            queue.append(e.right)
    return result
print(levelTraversal(drinks))
# print(hot.left.val)