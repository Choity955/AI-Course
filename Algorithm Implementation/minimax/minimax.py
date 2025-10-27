tree = {}
utilities = {}

n = int(input("Enter number of internal nodes with children: "))
for _ in range(n):
    data = input("Enter parent and its children separated by space: ").split()
    parent = data[0]
    children = data[1:]
    tree[parent] = children

m = int(input("Enter number of leaf nodes with utilities: "))
for _ in range(m):
    data = input("Enter leaf node and its utilities separated by space: ").split()
    leaf = data[0]
    util = list(map(int, data[1:]))
    utilities[leaf] = util

root = input("Enter root node: ")
root_type = input("Is root MAX or MIN? ").strip().upper()

def minimax(node, is_max):
    if node in utilities:
        val = max(utilities[node]) if is_max else min(utilities[node])
        return val, [node]

    if is_max:
        best_val = float('-inf')
        best_path = []
        for child in tree[node]:
            val, path = minimax(child, False)
            if val > best_val:
                best_val = val
                best_path = [node] + path
        return best_val, best_path
    else:
        best_val = float('inf')
        best_path = []
        for child in tree[node]:
            val, path = minimax(child, True)
            if val < best_val:
                best_val = val
                best_path = [node] + path
        return best_val, best_path

is_max_root = (root_type == "MAX")
best_value, best_path = minimax(root, is_max_root)

print("\nBest value for root ({}): {}".format(root_type, best_value))
print("Best path:", " -> ".join(best_path))