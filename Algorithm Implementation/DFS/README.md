# 🌲 Depth-First Search (DFS)

## 🧠 Overview
**Depth-First Search (DFS)** is a graph traversal algorithm that explores as far as possible along each branch before **backtracking**.  
It begins at a **source node** and explores one path completely before moving to the next.  
DFS can be implemented **recursively** or **using a stack** (LIFO – Last In, First Out).

---

## ⚙️ How DFS Works
### Step-by-Step Process:
1. **Start** from a source node.  
2. **Mark** the starting node as **visited**.  
3. **Explore** one of its unvisited neighbors.  
4. **Repeat** the process recursively (go deeper) until there are no unvisited neighbors.  
5. **Backtrack** to the previous node and continue exploring other unvisited neighbors.  
6. Continue until **all nodes** in the graph have been visited.

---

## 🧩 Example
If we start from node **A** in a connected graph:

**Traversal Order Example:**  
A → B → D → E → C → F  

DFS explores a path completely before returning (backtracking) to explore other branches.

---

## 🚀 Applications
- 🔹 Pathfinding in mazes and puzzles  
- 🔹 **Topological Sorting** (in Directed Acyclic Graphs)  
- 🔹 **Cycle Detection** in graphs  
- 🔹 **Finding connected components** in undirected graphs  
- 🔹 **Solving recursive problems** (e.g., Sudoku, N-Queens)  
- 🔹 AI and game trees (depth-based exploration)

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^m)` | **b** = branching factor, **m** = maximum depth of the search tree |
| **Space Complexity** | `O(b * m)` | Due to storage of nodes in the recursion stack or explicit stack |

---

## 🧮 Key Characteristics
- **Traversal Type:** Depth-order (go deep before backtracking)  
- **Data Structure Used:** Stack (explicit or recursion)  
- **Completeness:** ❌ No (infinite-depth graphs)  
- **Optimality:** ❌ No (does not always find the shortest path)  


# Input/Output Screenshot
