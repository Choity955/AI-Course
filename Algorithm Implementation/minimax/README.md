# 🎮 Minimax Algorithm

## 🧠 Overview
**Minimax** is a **decision-making algorithm** commonly used in **two-player, turn-based games** such as Tic-Tac-Toe, Chess, Checkers, or Connect Four.  

- One player is the **MAX** player, aiming to **maximize their score**.  
- The other is the **MIN** player, aiming to **minimize MAX's score**.  

The algorithm simulates all possible moves assuming both players play **optimally**, and determines the best move for the current player.

---

## ⚙️ How Minimax Works
### Step-by-Step Process:
1. **Construct** the game tree up to a certain depth.  
2. **Assign utility values** to terminal nodes:
   - Positive values → Favorable to **MAX**  
   - Negative values → Favorable to **MIN**  
3. **Propagate scores upward** in the tree:
   - **MAX nodes** select the **maximum value** among their children  
   - **MIN nodes** select the **minimum value** among their children  
4. The **root node value** represents the **best guaranteed outcome** for MAX if both players play optimally.  
5. **Choose the move** from the root that leads to this optimal outcome.

---

## 🧩 Example
For Tic-Tac-Toe:
- MAX = X, MIN = O  
- Minimax evaluates all possible moves up to a certain depth, calculating scores at terminal positions.  
- MAX picks the move that guarantees the **highest score**, anticipating MIN's optimal responses.

---

## 🚀 Applications
- 🎯 **Two-player games**: Tic-Tac-Toe, Chess, Connect Four  
- 📊 **Decision-making systems**: financial modeling, risk simulations  
- 🤖 **Adversarial planning**: planning for worst-case scenarios  
- 🧩 **AI planning in multi-agent robotics**: competitive or adversarial environments  

---

## ⏱️ Complexity Analysis
| Type | Complexity | Description |
|------|-------------|-------------|
| **Time Complexity** | `O(b^d)` | **b** = branching factor, **d** = depth of the game tree |
| **Space Complexity** | `O(b * d)` | Memory grows linearly with the depth in recursive implementation |

---

## 🧮 Key Features
- **Traversal Type:** Game tree evaluation (depth-first)  
- **Data Structure Used:** Recursive tree / Stack  
- **Completeness:** ✅ Yes (if the game tree is finite)  
- **Optimality:** ✅ Yes (guarantees the best move for MAX if both players play optimally)  
- **Drawback:** ⚠️ Exponential time complexity for large game trees  


# Input/Output Screenshot
<img width="544" height="247" alt="image" src="https://github.com/user-attachments/assets/8a834078-63ee-4c04-8a4b-e305792d4430" />.png

