import heapq

def a_star(graph, heuristics, start, goal):
    pq = [(heuristics[start], 0, start, [start])]
    visited = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path found:", " -> ".join(path))
            print("Cost:", g)
            return

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    print("No path found.")



graph = {}
heuristics = {}

nodes = input("Enter nodes (space separated): ").split()

for node in nodes:
    neighbors = input(f"Enter neighbors of {node} (format: node:cost ...): ").split()
    graph[node] = []
    for n in neighbors:
        if ":" in n:
            neigh, cost = n.split(":")
            graph[node].append((neigh, int(cost)))
    heuristics[node] = int(input(f"Heuristic of {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

a_star(graph, heuristics, start, goal)
