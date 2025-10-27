def bidirectional(graph, start, goal):
    f, b = {start}, {goal}
    while f and b:

        if f & b:
            return True

        f = {n for v in f for n in graph.get(v, [])} - f
        if f & b:
            return True

        b = {n for v in b for n in graph.get(v, [])} - b
    return False



graph = {}
n = int(input("Enter number of edges: "))
for i in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter start node: ")
goal = input("Enter goal node: ")


if bidirectional(graph, start, goal):
    print("Search met! Path exists.")
else:
    print("Search did not meet. No path exists.")
