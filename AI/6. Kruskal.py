
# Class to represent a graph
class Graph:
    # The __init__ method is the constructor of the Graph class
    def __init__(self, vertices):
        self.V = vertices   # initializes the number of vertices (self.V) and creates an empty list called self.graph
        self.graph = []     # self.graph to store the graph's edges


    # Function to add an edge to the graph
    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])


    # Function to find the parent of a vertex
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])


    # Function to perform union of two subsets
    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


    # Function to perform Kruskal's algorithm
    def kruskal_mst(self):
        result = []  # Stores the minimal spanning tree
        i = 0  # Index variable for sorted edges
        e = 0  # Index variable for result[]

        # Sort all the edges in ascending order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            # Pick the smallest edge and increment the index for the next iteration
            src, dest, weight = self.graph[i]
            i += 1

            root_src = self.find_parent(parent, src)
            root_dest = self.find_parent(parent, dest)

            # Check if including the current edge causes a cycle or not
            if root_src != root_dest:
                e += 1
                result.append([src, dest, weight])
                self.union(parent, rank, root_src, root_dest)

        # Print the minimal spanning tree
        print("Minimal Spanning Tree:")
        for src, dest, weight in result:
            print(f"{src} -- {dest} \tWeight: {weight}")


# Take input from the user
vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

# Create a graph object
graph = Graph(vertices)

# Input the edges and their weights
for i in range(edges):
    src, dest, weight = map(int, input("Enter source, destination, and weight of edge separated by spaces: ").split())
    graph.add_edge(src, dest, weight)

# Find and print the minimal spanning tree using Kruskal's algorithm
graph.kruskal_mst()