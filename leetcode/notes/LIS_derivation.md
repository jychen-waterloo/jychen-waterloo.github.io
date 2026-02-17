# Longest Increasing Subsequence (LIS) – Derivation Notes

## 1. Problem Restatement
Given an integer array `nums`, find the length of the longest strictly increasing subsequence (not necessarily contiguous). Classic examples:
- `[10,9,2,5,3,7,101,18]` → LIS length = 4 (`[2,3,7,101]`).

Two standard approaches:
1. Dynamic Programming `O(n^2)` – explicit state transitions, intuitive.
2. Patience Sorting / Binary Search `O(n log n)` – efficient, needs conceptual grounding.

These notes walk through both to reinforce *why* the `lower_bound` trick works and when to apply it.

---

## 2. O(n^2) DP – Building Intuition
**State**: `dp[i] =` length of LIS that *ends* at index `i` (i.e., `nums[i]` is the last element).

**Transition**:
```
dp[i] = 1 + max(dp[j]) for all j < i where nums[j] < nums[i]
if no such j, dp[i] = 1 (the subsequence is just nums[i])
```

**Answer**: `max(dp)` over all indices.

**Why it works**:
- Every LIS ending at `i` must come from some previous `j` whose value is smaller, so chaining lengths gives optimal substructure.
- Takes `O(n^2)` because each pair `(j,i)` might be checked.

**When to use**:
- When n ≤ 2e3, or when you need explicit LIS sequences (can backtrack parents stored in DP).

---

## 3. From DP to Patience Sorting Idea
Observation: In the DP table, we only care about the *best possible tail* for each length. If we know that the shortest possible tail for length `k` is value `x`, any longer LIS must be ≥ `k` and have tail ≥ `x`.

So we maintain an array `tails` (`dp` in your code) where:
- `tails[len-1] =` the **minimum possible tail value** for an increasing subsequence of length `len`.
- Always kept in **sorted order** (non-decreasing), because longer subsequences must have tails at least as large as shorter ones.

Steps for each `num`:
1. Use `lower_bound(tails.begin(), tails.end(), num)` to find first tail ≥ `num`.
2. If found inside array, replace it with `num` (better/ smaller tail for that length).
3. If not found (num > all tails), append to extend LIS.

**Why replacing works**:
- A smaller tail for the same length means more room to extend in the future. We’re not committing to actual subsequences, just keeping the best *options*.
- Because tails are sorted, binary search ensures `O(log n)` updates.

**Link to O(n^2) DP**:
- `tails[len-1]` essentially stores the minimum `nums[i]` among all `i` where `dp[i] = len`.
- Instead of scanning all previous `j`, we leverage the sorted property to jump to the right length directly.

---

## 4. Example Walkthrough
`nums = [10,9,2,5,3,7,101,18]`

```
Start: tails = []
num=10 → tails = [10]
num=9  → replace tails[0]=9 → [9]
num=2  → tails[0]=2 → [2]
num=5  → append → [2,5]
num=3  → replace tails[1]=3 → [2,3]
num=7  → append → [2,3,7]
num=101→ append → [2,3,7,101]
num=18 → replace tails[3]=18 → [2,3,7,18]
```
Length of tails = 4 → LIS length = 4 (one LIS is `[2,3,7,18]`).

Note we never explicitly built the subsequence; we only tracked feasible tails.

---

## 5. Reconstructing an Actual LIS (Optional)
To recover the sequence:
1. Run the `O(n^2)` DP with `parent[i]` storing the previous index chosen for `i`.
2. Alternatively, modify patience algorithm to keep parallel arrays of indices and parents (more bookkeeping, but doable).

Since interviews usually ask for length only, length-focused version is fine.

---

## 6. Practice Plan
1. Re-derive `dp[i]` transitions on paper for a small sample (size ≤ 6).
2. Implement `O(n^2)` version once, ensure you can narrate the recurrence.
3. Rewrite `O(n log n)` version *without* referencing template. Explain verbally:
   - “tails[k] stores the minimum possible tail for length k+1.”
   - “lower_bound finds the first tail ≥ current, meaning we can improve that length’s tail.”
4. Bonus: Write a tiny script to print `tails` after each step to visualize evolution.

---

## 7. Key Talking Points (for mock interview)
- Clarify difference between **subsequence** vs **substring**.
- Mention both `O(n^2)` and `O(n log n)` approaches and when each is appropriate.
- Explain the invariant: `tails` is strictly increasing in length, non-decreasing in values, storing *best tails*.
- Complexity: `O(n log n)` time due to binary searches, `O(n)` space.

Reviewing these notes plus coding both versions a couple more times should help cement the understanding beyond rote memory.
