
# used to find the vertex with the minimum key value among the vertices not yet included in the MST
def min_key(vertices, keys, mst_set):
    # mst_set (a boolean array indicating whether a vertex is already included in the MST or not). 
    min_key = float('inf')
    min_vertex = None
    for v in range(vertices):
        if keys[v] < min_key and not mst_set[v]:
            min_key = keys[v]
            min_vertex = v
    return min_vertex


# Function to print the minimal spanning tree
# parent (an array storing the parent of each vertex in the MST) and graph (the original graph)
def print_mst(parent, graph):
    print("Edge   Weight")
    for i in range(1, len(parent)):
        print(parent[i], "-", i, "  ", graph[i][parent[i]])


# Prim's algorithm for minimal spanning tree
def prim_mst(graph):
    vertices = len(graph) # Number of vertices in the graph

    # Initialize key values and MST set
    keys = [float('inf')] * vertices # float('inf') represents positive infinity, a special floating-point value that is greater than any other numerical value
    parent = [None] * vertices # the parent of each vertex in the MST (parent)
    mst_set = [False] * vertices

    # Starting vertex
    # The algorithm starts with the first vertex as the root. It sets its key value to 0 and parent to -1. The key values of all other vertices are set to infinity initially.
    keys[0] = 0
    parent[0] = -1

    for _ in range(vertices - 1):
        # Choose the vertex with the minimum key value
        u = min_key(vertices, keys, mst_set)

        # Add the chosen vertex to the MST set
        mst_set[u] = True

        # Update the key values of adjacent vertices
        for v in range(vertices):
            if graph[u][v] > 0 and not mst_set[v] and graph[u][v] < keys[v]:
                keys[v] = graph[u][v]
                parent[v] = u

    # Print the minimal spanning tree
    print_mst(parent, graph)

# Take input from the user for the graph
vertices = int(input("Enter the number of vertices: "))
graph = []
for _ in range(vertices):
    row = list(map(int, input("Enter the weights for the vertices separated by spaces: ").split()))
    graph.append(row)

# Find the minimal spanning tree using Prim's algorithm
prim_mst(graph)