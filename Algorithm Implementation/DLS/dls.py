def depth_limited_search(graph, start, goal, limit):
    explored = set()

    def recursive_dls(node, depth):
        if depth < 0:
            return None
        if node == goal:
            return [node]
        explored.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in explored:
                path = recursive_dls(neighbor, depth - 1)
                if path is not None:
                    return [node] + path
        return None

    return recursive_dls(start, limit)

graph = {}
n = int(input("Enter number of edges: "))
for i in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter start node: ")
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

result = depth_limited_search(graph, start, goal, limit)

if result:
    print("Path found:", " -> ".join(result))
else:
    print("No path found within the depth limit.")