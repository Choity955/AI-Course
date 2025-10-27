# 🔁 Iterative Deepening Search (IDS)

## 🧠 Overview
**Iterative Deepening Search (IDS)** is a search algorithm that combines the **space efficiency** of **Depth-First Search (DFS)** with the **completeness and optimality** of **Breadth-First Search (BFS)**.  

It works by repeatedly executing **Depth-Limited Search (DLS)** with increasing depth limits until the goal is found.  
In essence, IDS performs multiple DFS passes — each time allowing the search to go **one level deeper**.

---

## ⚙️ How the Algorithm Works
### Step-by-Step Process:
1. **Initialize** the depth limit to `0`.  
2. Perform **Depth-Limited Search (DLS)** up to the current depth limit.  
3. If the **goal is not found**:
   - **Increase** the depth limit by `1`.  
   - **Repeat** the DLS with the new limit.  
4. Continue until:
   - The **goal node** is found, or  
   - **All nodes** have been visited.  

---

## 🧩 Example
If the goal is at depth **d = 3**, IDS will run:
- DLS with limit = 0  
- DLS with limit = 1  
- DLS with limit = 2  
- DLS with limit = 3 → Goal found ✅  

Although earlier levels are re-searched, IDS remains efficient due to exponential reduction in nodes per level.

---

## 🚀 Applications
- 🔹 **Artificial Intelligence** search problems with **unknown solution depth**  
- 🔹 **Route-finding** algorithms  
- 🔹 **Puzzle solving** (e.g., 8-puzzle, Rubik’s Cube)  
- 🔹 **Game tree search** (e.g., chess, tic-tac-toe)  
- 🔹 **Robot motion planning** and navigation  

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^d)` | **b** = branching factor, **d** = depth of the goal node |
| **Space Complexity** | `O(b * d)` | Only a single path (plus siblings) is stored at any time |

---

## 🧮 Key Characteristics
- **Traversal Type:** Depth-first (iteratively deepened)  
- **Combines:** DFS efficiency + BFS completeness  
- **Completeness:** ✅ Yes  
- **Optimality:** ✅ Yes (for uniform step cost)  
- **Memory Efficiency:** ✅ Much better than BFS  
- **Drawback:** ⚠️ Repeated exploration of shallow nodes increases computation slightly  

---

> 💡 **Summary:**  
> Iterative Deepening Search is one of the most practical algorithms for problems with **large or infinite search spaces** and **unknown goal depth** — offering a balance between **speed, memory, and completeness**.


# Input/Output Screenshot
