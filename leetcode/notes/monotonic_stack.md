# Monotonic Stack 模板笔记 / Monotonic Stack Quick Notes

## 1) 什么时候考虑单调栈？/ When to use it?

**中文（速判信号）**
- 题目在问「下一个更大/更小元素」或「前一个更大/更小元素」。
- 需要对每个位置找“最近满足条件的元素”。
- 暴力是两层循环 `O(n^2)`，而且比较关系是可传递的（例如大小关系）。
- 常见关键词：next greater, previous smaller, daily temperatures, stock span, histogram。

**English (quick triggers)**
- You need **next/previous greater(or smaller) element**.
- For each index, find the **nearest index** satisfying a comparison.
- Brute force is `O(n^2)`, and comparisons are order-based/transitive.
- Typical keywords: next greater, previous smaller, daily temperatures, stock span, histogram.

---

## 2) 栈里放什么？/ What do we store in stack?

**中文**
- 大多数题目放**下标 index**（不是值），因为要计算距离、回填答案。
- 比较时用 `arr[stack.top()]` 和当前值比较。

**English**
- Usually store **indices**, not values, so you can compute distance and fill answers.
- Compare via `arr[stack.top()]` vs current value.

---

## 3) 核心流程模板 / Core template

### A) 下一个更大元素（如 739）/ Next Greater Element (e.g., 739)

```cpp
vector<int> ans(n, 0);
stack<int> st; // store indices, values are monotonic decreasing in stack

for (int i = 0; i < n; ++i) {
    while (!st.empty() && a[st.top()] < a[i]) {
        int j = st.top(); st.pop();
        ans[j] = i - j;  // or i / a[i], depending on problem
    }
    st.push(i);
}
```

**中文理解**：当前元素来“结算”之前比它小的元素。  
**English intuition**: current element resolves previous smaller unresolved indices.

### B) 下一个更小元素 / Next Smaller Element
- 把比较符号反过来：`a[st.top()] > a[i]`。

---

## 4) 单调方向怎么选？/ How to choose monotonic direction?

**中文**
- 求“下一个更大” → 维护**单调递减栈**（遇到更大就弹）。
- 求“下一个更小” → 维护**单调递增栈**（遇到更小就弹）。

**English**
- Next greater → maintain a **decreasing stack**.
- Next smaller → maintain an **increasing stack**.

---

## 5) 常见错误清单 / Common pitfalls

**中文**
1. 栈里放值导致无法算距离（应放 index）。
2. 比较符号写错（`<` / `<=` 取决于题目是否允许相等）。
3. 忘记在 `while` 后 `push(i)`。
4. 把“弹栈结算”写成只弹一次 `if`，而不是 `while`。

**English**
1. Storing values instead of indices.
2. Wrong comparator (`<` vs `<=`, depends on strict/non-strict requirement).
3. Forgetting `push(i)` after popping.
4. Using `if` instead of `while` when multiple items should be resolved.

---

## 6) 这题（739）的一句话复盘 / One-line recap for 739

**中文**：维护温度下标的递减栈，当前更高温度出现时持续弹栈并回填等待天数。  
**English**: Keep a decreasing stack of temperature indices; when a warmer day appears, pop and fill waiting days for all resolved indices.
