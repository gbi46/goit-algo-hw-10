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

# Monte Carlo Integration

This project demonstrates how to approximate definite integrals using the **Monte Carlo method** and compare the results against the exact solution computed with SciPy’s `quad` function.

---

## Method Explanation

The goal is to estimate the integral

\[
I = \int_a^b f(x)\,dx
\]

using random sampling.

1. **Generate random samples**  
   Draw `N` random points uniformly in the interval \([a, b]\).

2. **Evaluate the function**  
   Compute \( f(x) \) for each random point.

3. **Compute the mean**  
   Approximate the expected value of the function:
   \[
   \text{mean} \approx \frac{1}{N} \sum_{i=1}^N f(x_i)
   \]

4. **Scale by interval length**  
   Multiply the average by the interval width:
   \[
   I \approx (b-a) \cdot \text{mean}
   \]

5. **Accuracy**  
   - Improves as the number of samples increases (`N → ∞`).  
   - Error decreases roughly as \( 1/\sqrt{N} \).  
