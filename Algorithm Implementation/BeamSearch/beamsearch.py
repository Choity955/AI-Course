def beam_search(graph, heuristics, start, goal, beam_width):
    level = [(heuristics[start], [start])]

    while level:

        level = sorted(level, key=lambda x: x[0])[:beam_width]

        new_level = []
        for h, path in level:
            node = path[-1]
            if node == goal:
                print("Path found:", " -> ".join(path))
                return
            for neighbor in graph.get(node, []):
                new_level.append((heuristics[neighbor], path + [neighbor]))

        level = new_level

    print("No path found.")

graph = {}
heuristics = {}

nodes = input("Enter nodes (space separated): ").split()

for node in nodes:
    graph[node] = input(f"Neighbors of {node}: ").split()
    heuristics[node] = int(input(f"Heuristic of {node}: "))

start = input("Start node: ")
goal = input("Goal node: ")
beam_width = int(input("Enter beam width: "))

beam_search(graph, heuristics, start, goal, beam_width)
