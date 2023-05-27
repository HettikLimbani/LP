
import heapq

def astar(start, goal, graph):
    # graph (the graph represented as a dictionary of dictionaries, where each key represents a node and its value is a dictionary of its neighbors and their corresponding weights).
    # Initialize the open and closed lists
    open_list = [(0, start)]
    closed_list = set()

    # Initialize the path and cost dictionaries
    path = {start: None}
    cost = {start: 0}

    while open_list:
        # Get the node with the lowest cost from the open list
        current_cost, current_node = heapq.heappop(open_list)

        # Add the current node to the closed list
        closed_list.add(current_node)

        # Check if the goal node has been reached
        if current_node == goal:
            return reconstruct_path(path, start, goal)

        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the tentative cost from the start node to the neighbor node
            tentative_cost = cost[current_node] + weight

            # Check if the neighbor node is already in the closed list
            if neighbor in closed_list:
                continue

            # Check if the neighbor node is not in the open list or has a lower cost
            if neighbor not in [node for _, node in open_list] or tentative_cost < cost[neighbor]:
                # Update the path and cost dictionaries
                path[neighbor] = current_node
                cost[neighbor] = tentative_cost

                # Calculate the heuristic value for the neighbor node
                heuristic_value = heuristic(neighbor, goal)

                # Add the neighbor node to the open list with the combined cost and heuristic value
                heapq.heappush(open_list, (tentative_cost + heuristic_value, neighbor))

    # No path found
    return None

def reconstruct_path(path, start, goal):
    # Reconstruct the shortest path from the goal node to the start node
    current_node = goal
    path_nodes = []

    while current_node != start:
        path_nodes.append(current_node)
        current_node = path[current_node]

    # Add the start node to the path
    path_nodes.append(start)

    # Reverse the path to get the correct order
    path_nodes.reverse()

    return path_nodes

def heuristic(node, goal):
    # Calculate the Manhattan distance as the heuristic
    return abs(ord(node) - ord(goal))

# Function to input the graph from the user
def get_graph_from_user():
    graph = {}

    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        source = input("Enter the source node: ")
        target = input("Enter the target node: ")
        weight = int(input("Enter the weight: "))

        # Add the edge to the graph
        if source not in graph:
            graph[source] = {}
        graph[source][target] = weight

    return graph

# Example usage
graph = get_graph_from_user()

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
shortest_path = astar(start_node, goal_node, graph)

if shortest_path is None:
    print("No path found.")
else:
    print("Shortest path:", ' -> '.join(shortest_path))















'''The code begins by importing the heapq module, which provides an implementation of the heap queue algorithm used for efficient priority queue operations.

The astar function is defined, which takes three parameters: start (the starting node), goal (the goal node), and graph (the graph represented as a dictionary of dictionaries). The graph dictionary represents the nodes of the graph as keys, and the corresponding values are dictionaries of neighbor nodes and their weights.

Inside the astar function, the open and closed lists are initialized. The open list is a priority queue implemented as a heap, where each item is a tuple containing the cost and the node. The closed list is a set that keeps track of the visited nodes.

The path and cost dictionaries are initialized. The path dictionary stores the previous node in the shortest path to each node, and the cost dictionary stores the cost of the shortest path from the start node to each node.

The main loop of the A* algorithm starts with the while loop, which continues until the open list is empty.

Inside the loop, the node with the lowest cost is retrieved from the open list using heapq.heappop. This node becomes the current node for exploration.

The current node is added to the closed list.

If the current node is the goal node, the reconstruct_path function is called to reconstruct the shortest path from the start node to the goal node. The path is returned as the result.

If the goal node has not been reached, the algorithm explores the neighbors of the current node.

For each neighbor, the algorithm calculates the tentative cost from the start node to the neighbor node by adding the weight of the edge between them to the cost of the current node.

If the neighbor node is already in the closed list, it is skipped.

If the neighbor node is not in the open list or has a lower cost than previously calculated, the path and cost dictionaries are updated with the new values.

The heuristic value is calculated for the neighbor node using the heuristic function. In this implementation, the Manhattan distance between the neighbor node and the goal node is used as the heuristic.

The neighbor node is added to the open list with the combined cost and heuristic value, using heapq.heappush to maintain the priority order.

After the loop ends, if no path is found (i.e., the open list is empty), None is returned.

The reconstruct_path function takes three parameters: path (the dictionary containing the previous nodes), start (the starting node), and goal (the goal node). It reconstructs the shortest path from the goal node to the start node by following the previous nodes in the path dictionary.

The reconstructed path is reversed to get the correct order, and it is returned as a list of nodes.

The heuristic function calculates the Manhattan distance between a node and the goal node. It uses the ASCII values of the characters representing the nodes to calculate the absolute difference.

The get_graph_from_user function is defined to input the graph from the user. It prompts the user to enter the number of edges and then iteratively asks for the source node, target node, and weight of each edge. The graph is represented as a dictionary of dictionaries, where each key represents a node, and its value is a dictionary of its neighbors'''