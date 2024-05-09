def prim(graph, start=0):
    V = len(graph)
    visited = [False] * V  # Mark all vertices as not visited initially
    mst = []  # Initialize minimum spanning tree (MST)

    visited[start] = True  # Mark the starting vertex as visited
    while len(mst) < V - 1:  # Continue until MST has V-1 edges
        smallest = float('inf')  # Initialize smallest edge weight to infinity
        for u in range(V):  # Iterate through all vertices
            if visited[u]:  # Consider only visited vertices
                for v, weight in graph[u]:  # Iterate through neighbors of visited vertices
                    if not visited[v] and weight < smallest:
                        # If the neighbor is not visited and its weight is smaller than current smallest
                        smallest = weight  # Update smallest weight
                        min_edge = (u, v, smallest)  # Store the current minimum edge
        mst.append(min_edge)  # Add the smallest edge to the MST
        visited[min_edge[1]] = True  # Mark the neighbor of the smallest edge as visited

    return mst

# Example graph representation
graph = [
    # (neighbor, weight)
    [(1, 3), (2, 5)],  # 0
    [(0, 3), (2, 1), (3, 4)],  # 1
    [(0, 5), (1, 1), (3, 2)],  # 2
    [(1, 4), (2, 2)]   # 3
]

# Call prim function and print the resulting minimum spanning tree
mst = prim(graph)
print(mst)
