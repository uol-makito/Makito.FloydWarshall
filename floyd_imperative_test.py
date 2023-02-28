"""
Floyd's Shortest Path Algorithm (Imperative) Performance Test.
"""
import timeit
from datetime import datetime

SETUP = """
import sys
import itertools
"""

STMT = """
def floyd(distance):
    for intermediate, start_node,end_node \
    in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] +
                                             distance[intermediate][end_node])
    # print(distance)

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH = len(graph[0])

floyd(graph)
"""

NUMBER = 10000

# Print test message.
print("############################################################")
print("# Floyd's Shortest Path Algorithm (Imperative) Performance Test")
print(f"# Test Time (UTC): {datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')}")
print(f"# timeit() number = {NUMBER}")
print("############################################################")
# Run the test 20 times.
for i in range(20):
    print(f"Test attempt {i + 1}: {timeit.timeit(stmt = STMT, setup = SETUP, number = NUMBER):.6f}")
