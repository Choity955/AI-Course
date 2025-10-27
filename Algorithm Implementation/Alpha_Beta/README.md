# ✂️ Alpha-Beta Pruning Algorithm

## 🧠 Overview
**Alpha–Beta Pruning** is an **optimization of the Minimax algorithm** used in **two-player games**.  

- It **reduces the number of nodes** evaluated in the game tree by **pruning branches** that cannot possibly affect the final decision.  
- This allows the algorithm to **compute the optimal move faster** without exploring the entire tree.

---

## ⚙️ How the Algorithm Works
The algorithm maintains two parameters during traversal:

- **α (alpha):** The **best value MAX** can guarantee so far  
- **β (beta):** The **best value MIN** can guarantee so far  

### Tree Traversal Rules
- **At MAX nodes:** `α = max(α, currentValue)`  
- **At MIN nodes:** `β = min(β, currentValue)`  
- **Pruning Condition:** If `β ≤ α`, the remaining branches **cannot influence the outcome** and are **pruned**.

---

## 🔹 Step-by-Step Process
1. Start at the **root node** (initial game state).  
2. Initialize `α = -∞` and `β = +∞`.  
3. Apply **Minimax recursively**, but:
   - **Update α** when a MAX node improves its best value  
   - **Update β** when a MIN node improves its best value  
4. **Prune child nodes** when `β ≤ α`.  
5. Continue until the tree is **fully evaluated or pruned**.  
6. The **root value** gives the **best possible move** for the current player.

---

## 🧩 Applications
- 🎮 **Game AI** – faster and optimal move selection in Chess, Tic-Tac-Toe, Connect Four  
- 🤖 **Robotics** – minimize time for adversarial path planning  
- 📊 **Decision-making systems** – select best counter actions  
- 🛡️ **Security AI** – plan defense strategies against adversarial agents  

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^(d/2))` | Reduces the effective branching factor by pruning irrelevant nodes |
| **Space Complexity** | `O(b * d)` | Memory needed for recursive stack or explicit tree traversal |

---

## 🧮 Key Features
- **Traversal Type:** Optimized game tree evaluation (depth-first)  
- **Data Structure Used:** Recursive tree / Stack  
- **Completeness:** ✅ Yes (pruning does not affect correctness)  
- **Optimality:** ✅ Yes (returns the same move as full Minimax)  
- **Efficiency:** ⚡ Reduces computation time significantly compared to standard Minimax  

# Input/Output Screenshot
<img width="645" height="368" alt="image" src="https://github.com/user-attachments/assets/2a77d344-91a8-4fc3-a56b-4ef7a432a000" />.png

