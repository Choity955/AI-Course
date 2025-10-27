import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = [(heuristics[start], start, [start])]

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == goal:
            print("Path found:", " -> ".join(path))
            return
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))
    print("No path found.")

graph = {}
heuristics = {}

nodes = input("Enter nodes (space separated): ").split()

for node in nodes:
    graph[node] = input(f"Neighbors of {node}: ").split()
    heuristics[node] = int(input(f"Heuristic of {node}: "))

start = input("Start node: ")
goal = input("Goal node: ")

best_first_search(graph, heuristics, start, goal)