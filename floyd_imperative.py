"""
Floyd's Shortest Path Algorithm (Imperative).
"""
import sys
import itertools

def floyd(distance):
    """
    Main function for Floyd's Shortest Path Algorithm.

    This function updates a distance matrix to contain the shortest path
    between every pair of vertices in the graph.

    Parameters:
    distance (list): A 2D list representing the input graph as an adjacency matrix.

    Returns:
    None: The function updates the distance matrix in place.
    """
    # For each intermediate vertex, find the shortest path between all pairs of vertices.
    for intermediate, start_node,end_node \
    in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same,
        # then the distance would be zero.
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # Return all possible paths and find the minimum.
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] +
                                             distance[intermediate][end_node])
    # Any value that have sys.maxsize has no path.
    print(distance)

# Define a constant for the maximum distance.
NO_PATH = sys.maxsize

# Define the input graph as an adjacency matrix.
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

# Get the number of vertices in the graph.
MAX_LENGTH = len(graph[0])

# Call the floyd function with the input graph.
floyd(graph)
