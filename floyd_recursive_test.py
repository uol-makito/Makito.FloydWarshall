"""
Floyd's Shortest Path Algorithm (Recursive) Performance Test.
"""
import timeit
from datetime import datetime

SETUP = """
import sys
"""

STMT = """
def floyd(distance):
    max_length = len(distance)
    for intermediate in range(max_length):
        for start_node in range(max_length):
            for end_node in range(max_length):
                if start_node == end_node:
                    distance[start_node][end_node] = 0
                    continue
                distance[start_node][end_node] = floyd_helper(
                    distance, intermediate, start_node, end_node)
    # print(distance)

def floyd_helper(distance, intermediate, start_node, end_node):
    if intermediate == 0:
        return distance[start_node][end_node]
    return min(floyd_helper(distance, intermediate - 1, start_node, end_node),
               floyd_helper(distance, intermediate - 1, start_node, intermediate) +
               floyd_helper(distance, intermediate - 1, intermediate, end_node))

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

floyd(graph)
"""

NUMBER = 10000

# Print test message.
print("############################################################")
print("# Floyd's Shortest Path Algorithm (Recursive) Performance Test")
print(f"# Test Time (UTC): {datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')}")
print(f"# timeit() number = {NUMBER}")
print("############################################################")
# Run the test 20 times.
for i in range(20):
    print(f"Test attempt {i + 1}: {timeit.timeit(stmt = STMT, setup = SETUP, number = NUMBER):.6f}")
