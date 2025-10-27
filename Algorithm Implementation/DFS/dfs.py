def dfs(adj, node, visited):
    visited[node] = True
    print(node, end=" ")

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(adj, neighbor, visited)

def main():
    n = int(input("Enter number of vertices: "))
    adj = [[] for _ in range(n)]

    e = int(input("Enter number of edges: "))
    print("Enter edges (format: u v):")
    for i in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    start = int(input("Enter starting vertex for DFS: "))
    visited = [False] * n
    print("DFS traversal starting from vertex", start, ":")
    dfs(adj, start, visited)

if __name__ == "__main__":
    main()