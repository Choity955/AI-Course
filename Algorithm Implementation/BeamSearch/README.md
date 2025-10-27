# 🎯 Beam Search

## 🧠 Overview
**Beam Search** is a **heuristic search algorithm** similar to **Best-First Search**, but it only keeps a **fixed number of the best nodes** at each level — called the **beam width (k)**.  

- Reduces memory usage compared to Best-First Search.  
- Does **not guarantee an optimal solution**, but is much faster for large search spaces.  

---

## ⚙️ How the Algorithm Works
### Step-by-Step Process:
1. **Start** with the initial node.  
2. **Generate** all successors of the current node.  
3. **Evaluate** each successor using a **heuristic function `h(n)`** (estimate of closeness to the goal).  
4. **Sort** the successors by heuristic value (best first).  
5. **Keep only the top `k` nodes** — this is the **beam width**.  
6. **Expand** these `k` nodes in the next iteration.  
7. **Repeat** until:
   - The **goal is found**, or  
   - There are **no nodes left** to expand.

---

## 🧩 Applications
1. **Natural Language Processing (NLP)** – machine translation, sentence generation  
2. **Speech Recognition** – predicting most likely word sequences  
3. **Game AI** – efficiently predicting best moves in large game trees  
4. **Robot Path Planning** – exploring large state spaces without memory explosion  

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b * d)` for small beam width (`k << b`) | Expands only top `k` nodes at each level |
| **Space Complexity** | `O(k * d)` | Stores only the best `k` nodes per level |

---

## 🧮 Key Characteristics
- **Traversal Type:** Heuristic-guided, limited width  
- **Data Structure Used:** Priority queue / sorted list of top nodes  
- **Completeness:** ❌ Not guaranteed  
- **Optimality:** ❌ Not guaranteed  
- **Memory Efficient:** ✅ Only top `k` nodes are stored at each level  

---

> 💡 **Summary:**  
> Beam Search trades **optimality** for **efficiency** by exploring only the most promising nodes at each level.  
> It is widely used in **NLP, speech recognition, AI game search, and robotics** when the search space is too large for full Best-First Search.


# Input/Output Screenshot
<img width="356" height="420" alt="image" src="https://github.com/user-attachments/assets/2411baf6-160d-4097-9a64-172ffe744620" />.png

