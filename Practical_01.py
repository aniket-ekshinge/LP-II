from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs_recursive(self, queue, visited=None):
        if not queue:
            return
        vertex = queue.pop(0)
        print(vertex, end=' ')
        if visited is None:
            visited = set()
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
        self.bfs_recursive(queue, visited)

if __name__ == "__main__":
    g = Graph()
    n = int(input("Enter the number of edges: "))

    for _ in range(n):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)

    start_vertex = int(input("Enter the starting vertex: "))

    print("Depth First Search (DFS):")
    g.dfs_recursive(start_vertex)
    print("\n")

    print("Breadth First Search (BFS):")
    g.bfs_recursive([start_vertex])
