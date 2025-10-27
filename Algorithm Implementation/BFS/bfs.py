from collections import dq

def bfs(adj, s):
    v = [False] * len(adj)
    q = dq([s])
    v[s] = True
    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor in adj[node]:
            if not v[neighbor]:
                v[neighbor] = True
                q.append(neighbor)

def main():
    n = int(input("Enter number of vertices: "))

    adj = [[] for _ in range(n)]

    e = int(input("Enter number of edges: "))

    print("Enter edges (u v) where u and v are vertex indices starting from 0:")

    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    s = int(input("Enter starting vertex for BFS: "))

    print("BFS traversal starting from vertex", s, ":")
    bfs(adj, s)

if __name__ == "__main__":
    main()