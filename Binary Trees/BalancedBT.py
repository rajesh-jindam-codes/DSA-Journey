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
    def balanceCheck(self,node):
        if node==None:
            return 0
        leftHeight=self.balanceCheck(node.left)
        if leftHeight==-1:
            return -1
        rightHeight=self.balanceCheck(node.right)
        if rightHeight==-1:
            return -1
        if abs(leftHeight-rightHeight)>1:
            return -1
        return 1+max(leftHeight,rightHeight)
    def isBalanced(self,root):
        x=self.balanceCheck(root)
        if x==-1:
            return False
        return True
obj=Solution()
print(obj.isBalanced(drinks))