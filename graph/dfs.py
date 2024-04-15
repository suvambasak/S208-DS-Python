class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                if vertex in self.graph:
                    stack.extend(reversed(self.graph[vertex]))


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS Recursive Traversal starting from vertex 2:")
g.dfs_recursive(2)
print("\nDFS Iterative Traversal starting from vertex 2:")
g.dfs_iterative(2)


# (base) suvam@KD-304G:/mnt/Storage/Repositories/S208-DS-Python$ /bin/python /mnt/Storage/Repositories/S208-DS-Python/graph/dfs.py
# DFS Recursive Traversal starting from vertex 2:
# 2 0 1 3
# DFS Iterative Traversal starting from vertex 2:
# 2 0 1 3
