# 🔄 Bidirectional Search

## 🧠 Overview
**Bidirectional Search** is an efficient search algorithm used to find the **shortest path** between a **start node** and a **goal node** in a graph.  
Instead of searching from one direction like BFS or DFS, it runs **two simultaneous searches**:
- One **forward** from the **start node**  
- One **backward** from the **goal node**

When the two searches meet in the middle, the algorithm terminates — significantly reducing the **search space** and improving efficiency.

---

## ⚙️ How the Algorithm Works
### Step-by-Step Process:
1. **Initialize** two queues: one for the **forward search** and one for the **backward search**.  
2. **Perform BFS** from both sides alternately (expand one level from each direction).  
3. After each expansion, **check if any node** has been visited by both searches.  
4. If a **common node** is found → the path between start and goal exists.  
5. **Combine** the two partial paths (from start → meeting point and from goal → meeting point).  
6. **Stop** the algorithm once the connection is made.

---

## 🧩 Example
For a graph with start node **S** and goal node **G**,  
Bidirectional Search runs:
- BFS from **S → ... → M**  
- BFS from **G → ... → M**  
When both searches meet at node **M**, the algorithm reconstructs the **shortest path S → M → G**.

---

## 🚀 Applications
- 🗺️ **Route finding** in maps and navigation systems (e.g., Google Maps, GPS)  
- 👥 **Social network analysis** — finding the shortest link between two people  
- 🤖 **Robot motion planning** — optimizing pathfinding between two locations  
- 🎮 **AI in games** — computing efficient paths in puzzles or game trees  

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^(d/2))` | Much faster than BFS (`O(b^d)`) since the search space grows in both directions |
| **Space Complexity** | `O(b^(d/2))` | Memory is required for both forward and backward searches |

---

## 🧮 Key Characteristics
- **Traversal Type:** Two-way (forward and backward BFS)  
- **Data Structure Used:** Two Queues  
- **Completeness:** ✅ Yes (if branching factor is finite)  
- **Optimality:** ✅ Yes (for unweighted graphs)  
- **Efficiency:** ⚡ Significantly better than single-direction BFS for large graphs  

---

> 💡 **Summary:**  
> Bidirectional Search is one of the most efficient algorithms for shortest path problems.  
> By searching from both ends simultaneously, it reduces time complexity from **O(b^d)** to **O(b^(d/2))**, making it ideal for large and sparse search spaces.


# Input/Output Screenshot
