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
class Solution:
    def __init__(self):
        self.diameter=0
    def calculateDiameter(self,node):
        if node==None:
            return 0
        leftHeight=self.calculateDiameter(node.left)
        rightHeight=self.calculateDiameter(node.right)
        self.diameter=max(self.diameter,leftHeight+rightHeight)
        return 1+max(leftHeight,rightHeight)
    def diameterofBT(self,node):
        self.diameter=0
        self.calculateDiameter(node)
        return self.diameter
obj=Solution()
print(obj.diameterofBT(drinks))