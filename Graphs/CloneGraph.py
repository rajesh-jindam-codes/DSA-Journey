from collections import deque

class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        # Create clone of starting node
        visited[node] = Node(node.val)

        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:

                # If neighbor hasn't been cloned
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)

                # Connect cloned current node to cloned neighbor
                visited[curr].neighbors.append(visited[nei])

        return visited[node]
adjList = [[2,4],[1,3],[2,4],[1,3]]
# Create the original graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]


# Clone graph
obj = Solution()
clone = obj.cloneGraph(node1)

# Check result
print(clone.val)
print([neighbor.val for neighbor in clone.neighbors])