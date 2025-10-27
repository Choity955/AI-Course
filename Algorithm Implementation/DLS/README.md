# 🌌 Depth-Limited Search (DLS)

## 🧠 Overview
**Depth-Limited Search (DLS)** is a variation of **Depth-First Search (DFS)** where the search depth is **restricted to a fixed limit**.  
This restriction prevents the algorithm from going infinitely deep in cyclic or very large graphs.  
DLS is particularly useful when the **goal node is known to be within a certain depth** from the starting node.

---

## ⚙️ How the Algorithm Works
### Step-by-Step Process:
1. **Start** from the source node.  
2. **Keep track** of the current depth during traversal.  
3. If the **current depth > limit**, **stop exploring** that path (return).  
4. **Visit** the node and mark it as **visited**.  
5. For each **unvisited neighbor**, **recursively perform DLS** with the depth incremented by one.  
6. Continue until:
   - The **goal node is found**, or  
   - The **depth limit is reached**.

---

## 🧩 Example
Suppose the depth limit is **3** — DLS will explore all paths up to that depth and **stop** even if the goal lies deeper.  
If the goal is not found, the algorithm terminates without success.

---

## 🚀 Applications
- 🔹 Avoiding **infinite loops** in deep or cyclic graphs  
- 🔹 **Robot path planning** where exploration is limited to nearby areas  
- 🔹 Used as the **basis of Iterative Deepening Search (IDS)**  
- 🔹 **Game tree exploration** — exploring a limited number of moves ahead  

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^l)` | **b** = branching factor, **l** = depth limit |
| **Space Complexity** | `O(b * l)` | Memory grows linearly with the depth limit |

⚠️ **Limitation:**  
DLS may **miss the goal** if it lies **beyond the depth limit**, but it offers significant **time and space savings** compared to full DFS.

---

## 🧮 Key Characteristics
- **Traversal Type:** Depth-first (with cutoff)  
- **Data Structure Used:** Stack / Recursion  
- **Completeness:** ❌ No (if goal is deeper than limit)  
- **Optimality:** ❌ No (depends on depth limit selection)  


# Input/Output Screenshot
<img width="460" height="311" alt="image" src="https://github.com/user-attachments/assets/d7a3bbef-5db4-4232-b30d-eb2d4f2348d9" />.png
<img width="392" height="345" alt="image" src="https://github.com/user-attachments/assets/325ca42f-533d-4909-9771-6d451cc52dad" />.png

