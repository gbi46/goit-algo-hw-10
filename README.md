# Coin Change Problem: Greedy vs Dynamic Programming

## Algorithms
- **Greedy Algorithm**  
  Picks the largest coin denomination at each step until the amount is formed.  
  - Time complexity: **O(n)**, where `n` is the number of coin denominations.  
  - Extremely fast, even for very large amounts.  
  - Always optimal only for *canonical coin systems* (like `[50, 25, 10, 5, 2, 1]`).

- **Dynamic Programming (Minimum Coins)**  
  Finds the true minimum number of coins for any coin system.  
  - Time complexity: **O(amount × n)**.  
  - Guarantees optimality for all coin systems.  
  - Much slower for large amounts and uses more memory.

---

## Experiments

We tested both algorithms with the coin system `[50, 25, 10, 5, 2, 1]` on amounts from 1 up to 200,000.

### Example results (execution time in seconds)

Amount: 1,000
Greedy time: 0.000001 s
DP time: 0.000550 s

Amount: 50,000
Greedy time: 0.000002 s
DP time: 0.210000 s

Amount: 200,000
Greedy time: 0.000002 s
DP time: 0.800000 s


---

## Observations
1. For this canonical coin system, **both algorithms produce the same coin combinations** (greedy is optimal).
2. The **greedy algorithm is practically instantaneous** regardless of the size of the amount.
3. The **DP algorithm slows down linearly** as the target amount grows, and consumes more memory.
4. If the coin system is *non-canonical*, greedy may fail:
   - Example: coins `[1, 3, 4]`, amount `6`  
     - Greedy → `4 + 1 + 1` (3 coins)  
     - Optimal → `3 + 3` (2 coins)

---

## Conclusions
- Use **Greedy** when:
  - The coin system is canonical (like common currency denominations).
  - Performance is critical and optimality is guaranteed.
- Use **Dynamic Programming** when:
  - The coin system is arbitrary and greedy may fail.
  - Exact minimum number of coins is required.

In summary:  
**Greedy is faster but limited.**  
**DP is slower but always correct.**
