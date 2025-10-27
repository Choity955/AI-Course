# 🌐 Breadth-First Search (BFS)

## 🧠 Overview
**Breadth-First Search (BFS)** is a fundamental graph traversal algorithm used to explore nodes and edges systematically.  
It starts from a **source node** and explores all its **immediate neighbors (same level)** before moving to nodes at the next level.  
BFS uses a **queue (FIFO – First In, First Out)** data structure to keep track of the next node to visit.

---

## ⚙️ How BFS Works
### Step-by-Step Process:
1. **Start** with a source node and mark it as **visited**.  
2. **Enqueue** the source node into a queue.  
3. **While the queue is not empty:**
   - **Dequeue** a node from the front of the queue.  
   - Visit all **unvisited neighbors** of that node.  
   - **Mark** each neighbor as visited and **enqueue** them.  
4. Continue until the queue becomes empty — meaning all reachable nodes have been visited.

---

## 🧩 Example
If we start from node **A** in a connected graph:

**Traversal Order:**  
A → B → C → D → E → F

Each node at the same depth level is explored before moving deeper.

---

## 🚀 Applications
- 🔹 Finding the **shortest path** in unweighted graphs.  
- 🔹 **Web crawling** – exploring links level by level.  
- 🔹 **Network broadcasting** – sending data to all reachable nodes.  
- 🔹 **Social networks** – finding the connection path between users (e.g., degrees of separation).  
- 🔹 **AI and game trees** – exploring all possible moves level by level.

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^d)` | Where **b** = branching factor, **d** = depth of the shallowest goal node |
| **Space Complexity** | `O(b^d)` | Due to storage of all nodes at the current level in the queue |

---

## 🧮 Key Characteristics
- **Traversal Type:** Level-order (breadth-first)
- **Data Structure Used:** Queue (FIFO)
- **Completeness:** ✅ Yes (if branching factor is finite)
- **Optimality:** ✅ Yes (for unweighted graphs)


# Input/Output Screenshot
<img width="332" height="237" alt="image" src="https://github.com/user-attachments/assets/f942bb95-1ba7-4633-85e4-ec80acc0fcc7" />.png

