class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def serialize(self,root):
        result=[]
        def dfs(node):
            if node is None:
                result.append("N")
                return 
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)
    def deserialize(self,data):
        values=data.split(",")
        index=[0]
        def dfs():
            if values[index[0]]=='N':
                index[0]+=1
                return None
            node=TreeNode(int(values[index[0]]))
            index[0]+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
obj=Solution()
root= TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(4)
root.right.right=TreeNode(5)

print(obj.serialize(root))
print(obj.deserialize(obj.serialize(root)).val)