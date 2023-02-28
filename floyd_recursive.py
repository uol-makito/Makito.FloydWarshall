"""
Floyd's Shortest Path Algorithm (Recursive).
"""
import sys

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
    # Get the number of vertices in the graph.
    max_length = len(distance)
    # Iterate over all possible intermediate nodes.
    for intermediate in range(max_length):
        # Iterate over all possible start nodes.
        for start_node in range(max_length):
            # Iterate over all possible end nodes.
            for end_node in range(max_length):
                # If the start and end nodes are the same,
                # set the distance to 0 and continue to the next iteration.
                if start_node == end_node:
                    distance[start_node][end_node] = 0
                    continue
                # Use the floyd_helper function to update the distance matrix
                # with the shortest path between the start and end nodes
                # via the current intermediate node.
                distance[start_node][end_node] = floyd_helper(
                    distance, intermediate, start_node, end_node)
    # Print the updated distance matrix.
    print(distance)


def floyd_helper(distance, intermediate, start_node, end_node):
    """
    Helper function for Floyd's Shortest Path Algorithm.

    Recursively calculates the shortest path between two nodes
    using a given intermediate node.

    Parameters:
    distance (list): A 2D list representing the input graph as an adjacency matrix.
    intermediate (int): Index of the intermediate node being considered.
    start_node (int): Index of the starting node.
    end_node (int): Index of the ending node.

    Returns:
    int: The shortest distance between the starting node and the ending node
    via the given intermediate node.
    """
    # Base case: if the intermediate node is 0, return the distance between the start and end nodes.
    if intermediate == 0:
        return distance[start_node][end_node]
    # Recursive case: use the floyd_helper function to recursively calculate
    # the shortest path between the start and end nodes via the current intermediate node.
    return min(floyd_helper(distance, intermediate - 1, start_node, end_node),
               floyd_helper(distance, intermediate - 1, start_node, intermediate) +
               floyd_helper(distance, intermediate - 1, intermediate, end_node))


# Define a constant for the maximum distance.
NO_PATH = sys.maxsize

# Define the input graph as an adjacency matrix.
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

# Call the floyd function with the input graph.
floyd(graph)
