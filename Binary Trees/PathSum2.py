from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)

            # Leaf node
            if node.left is None and node.right is None:
                if remaining == node.val:
                    result.append(path[:])

            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)

            # Backtracking
            path.pop()

        dfs(root, targetSum, [])

        return result
    def buildTree(self,list):
        if not list:
            return None
        root=TreeNode(list[0])
        queue=deque([root])
        i=1
        while queue and i<len(list):
            node=queue.popleft()
            if list[i] is not None:
                node.left=TreeNode(list[i])
                queue.append(node.left)
            i+=1
            if i<len(list) and list[i] is not None:
                node.right=TreeNode(list[i])
                queue.append(node.right)
            i+=1
        return root
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]



targetSum = 22

obj = Solution()
root = obj.buildTree(root)
print(obj.pathSum(root, targetSum))
