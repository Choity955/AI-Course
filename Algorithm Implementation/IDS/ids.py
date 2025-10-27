def dls(node, goal, depth, graph,):

    if depth == 0 and node == goal:
        return [node]
    if depth > 0:

        for child in graph.get(node, []):
            path = dls(child, goal, depth - 1, graph)
            if path:
                return [node] + path

    return None

def ids(start, goal, graph, max_depth):
    for depth in range(max_depth + 1):
        path = dls(start, goal, depth, graph)
        if path:
            return path
    return None

graph = {}
n = int(input("Enter the number of edges in the graph: "))
print("Enter edges in format: node parent_node ( A B)")
for _ in range(n):
    parent, child = input().split()
    if parent in graph:
        graph[parent].append(child)
    else:
        graph[parent] = [child]

s = input("Enter the start node: ")
gl = input("Enter the goal node: ")
m = int(input("Enter maximum search depth: "))

path = ids(s, gl, graph, m)
if path:
    print("Path found:", path)
else:
    print("No path found")
