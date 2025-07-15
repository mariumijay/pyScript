

#01 Breadth-First Search

from collections import deque

# Breadth-First Search Function
def bfs(graph, start_node):
    visited = set()                      # Set to keep track of visited nodes
    queue = deque([start_node])         # Queue for BFS initialized with start_node

    print("BFS Traversal Order:")

    while queue:
        current = queue.popleft()       # Dequeue a node from front
        if current not in visited:
            print(current, end=" ")     # Visit the node
            visited.add(current)        # Mark as visited

            # Add all unvisited neighbours to the queue
            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the BFS function
bfs(graph, 'A')

#02 Depth-First Search
# Depth-First Search Function
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()                 # Set to store visited nodes

    if node not in visited:
        print(node, end=" ")           # Visit the node
        visited.add(node)              # Mark as visited

        # Recursively visit all unvisited neighbours
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the DFS function
print("DFS Traversal Order:")
dfs(graph, 'A')


