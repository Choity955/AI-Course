# ⭐ A* Algorithm

## 🧠 Overview
**A\*** is an **informed search algorithm** that finds the **shortest (optimal) path** from a start node to a goal node.  

It combines:  
- **Actual cost so far:** `g(n)` – cost from the start node to the current node `n`  
- **Estimated cost to goal:** `h(n)` – heuristic estimate from `n` to the goal  

The total estimated cost is:  

f(n) = g(n) + h(n)


- **f(n):** Total estimated cost through node `n`  
- The algorithm **expands the node with the lowest f(n) first**, efficiently guiding the search toward the goal.

---

## ⚙️ How A* Works
### Step-by-Step Process:
1. **Initialize**
   - Create an **OPEN list** (priority queue) for nodes to explore.  
   - Create a **CLOSED list** for nodes already explored.  
   - Add the **start node** to OPEN with `f(start) = g(start) + h(start)`.  

2. **Loop**
   - Pick the node `n` from OPEN with the **lowest f(n)**.  
   - If `n` is the **goal**, stop — the optimal path is found.  
   - Move `n` to the CLOSED list.  
   - For each neighbor of `n`:
     - Calculate `g(neighbor) = g(n) + cost(n, neighbor)`  
     - Calculate `h(neighbor)` (heuristic estimate to goal)  
     - Calculate `f(neighbor) = g(neighbor) + h(neighbor)`  
     - If the neighbor is in OPEN or CLOSED **with a lower f value**, skip it.  
     - Otherwise, **add or update** it in the OPEN list.  

3. **Repeat** until:
   - The **goal is found**, or  
   - OPEN list is empty (no path exists).  

---

## 🧩 Applications
- 🗺️ **Pathfinding in games** (Pac-Man, Google Maps)  
- 🤖 **Robot navigation**  
- 🛣️ **Route optimization**  
- 🧩 **AI planning and puzzle solving** (e.g., 8-puzzle)  

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^d)` | **b** = branching factor, **d** = depth of the solution |
| **Space Complexity** | `O(b^d)` | Stores all generated nodes in memory |

---

## 🧮 Key Features
- **Traversal Type:** Heuristic-guided graph search  
- **Data Structure Used:** Priority Queue (OPEN list)  
- **Completeness:** ✅ Yes (if branching factor is finite and h(n) is admissible)  
- **Optimality:** ✅ Yes (for **admissible and consistent heuristics**)  
- **Efficiency:** ⚡ Expands fewer nodes than BFS by using a heuristic  

# Input/Output Screenshot
![ Input_Output_Screenshot]<img width="348" height="507" alt="image" src="https://github.com/user-attachments/assets/434a7343-6745-4515-acbb-f2e305631a1d" />.png
