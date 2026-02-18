# 0/1 Knapsack Pattern Cheat Sheet

> Covering classic problems like Partition Equal Subset Sum (416), Target Sum (494), and variations where each element can be **picked at most once**.

---

## 1. Core Problem Template
Given an array `nums` (usually positive ints) and a limit `capacity` (sum, weight, etc.), determine whether / how many ways / max value you can achieve by picking each `nums[i]` **at most once**.

Key characteristics:
- Decision per item is binary → either take it or skip it.
- State depends on prefix of items + remaining capacity.
- Transition resembles classic knapsack recurrence.

---

## 2. DP State Design
Two common formulations:

### a. Boolean Feasibility
`dp[i][c] = true` if using first `i` items you can reach sum `c`.
- Transition: `dp[i][c] = dp[i-1][c] OR dp[i-1][c - nums[i-1]]` (when `c >= nums[i-1]`).
- Base: `dp[0][0] = true` (use zero items to reach sum 0).

### b. Integer Optimization / Counting
`dp[i][c]` can represent maximum value achievable with capacity `c`, or number of ways to reach `c`. Transition adjusts accordingly.

For interview problems with `n ≤ 200` and `target ≤ 10^4`, Boolean DP is usually enough.

---

## 3. 1D Compression & Why Reverse Loops Matter
We often compress to 1D: `dp[c]` represents the current row (using items processed so far).

```cpp
vector<bool> dp(target + 1, false);
dp[0] = true;
for (int num : nums) {
    for (int c = target; c >= num; --c) {
        dp[c] = dp[c] || dp[c - num];
    }
}
```

**Why iterate `c` downward?**
- If we loop upward, `dp[c - num]` might have been updated **this round**, meaning we would use the same item twice (accidentally turning it into an unbounded knapsack). Traversing from high to low ensures each item contributes at most once.

Mnemonic: *0/1 knapsack ⇒ reverse loop; unbounded knapsack ⇒ forward loop.*

---

## 4. Template Breakdown (Partition Equal Subset Sum as Example)
1. Compute total sum. If odd → impossible.
2. Target = total / 2.
3. Initialize `dp[0] = true`.
4. For each `num`, update `dp` in reverse.
5. Answer = `dp[target]`.

**Annotated snippet:**
```cpp
bool canPartition(vector<int>& nums) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if (total % 2) return false;
    int target = total / 2;

    vector<bool> dp(target + 1, false);
    dp[0] = true;  // sum 0 achievable with empty subset

    for (int num : nums) {
        for (int c = target; c >= num; --c) {
            if (dp[c - num]) dp[c] = true;
        }
    }
    return dp[target];
}
```

---

## 5. Debug Checklist
- ✅ **Base case**: `dp[0] = true` (or 0 value) before processing items.
- ✅ **Bounds**: inner loop starts at `target` down to `num` (avoid negative index).
- ✅ **Order**: reverse loop for 0/1; forward only if repetition allowed.
- ✅ **Overflow**: when using sums, ensure target size manageable (`target ≤ 10^5`).
- ✅ **Early exit**: when target reached, optional optimization to stop.

---

## 6. Extensions
| Variant | Change |
|--------|--------|
| **Target Sum (494)** | Convert to subset sum by noting positive-negative partition: target becomes `(sum + S)/2`. Use same DP counting ways (integer DP). |
| **Last Stone Weight II (1049)** | Also reduces to partition into two subsets minimizing diff; same `target = total/2`, track closest achievable sum. |
| **On/Off Switch Problem** | When `nums` are weights and `values` separate, maintain `dp[c] = max value`. Transition: `dp[c] = max(dp[c], dp[c - weight] + value)`. |
| **Count ways** | Use integer DP array: `dp[c] += dp[c - num]` when iterating downward. |

---

## 7. Practice Playlist
1. 416. Partition Equal Subset Sum – boolean feasibility.
2. 1049. Last Stone Weight II – minimize difference.
3. 494. Target Sum – convert to subset sum counting.
4. 698. Partition to K Equal Sum Subsets – adds backtracking + pruning (conceptually related).
5. 474. Ones and Zeroes – 2D knapsack (`dp[zeros][ones]`).

Do a spaced repetition pass: Day 0 (today), Day 2, Day 5. Each pass: explain the reverse loop reasoning aloud before coding.

---

## 8. Interview Talking Points
- Define 0/1 vs unbounded knapsack succinctly.
- Mention state compression trade-offs.
- Explain how boolean DP turns decision problems into straightforward loops.
- Highlight debugging aids (e.g., printing dp after each item for small cases).

Keep this note handy whenever a “pick subset to reach X” problem appears; it’s almost always a 0/1 knapsack in disguise.
