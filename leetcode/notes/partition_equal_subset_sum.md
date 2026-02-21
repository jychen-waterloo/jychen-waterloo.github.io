# Partition Equal Subset Sum — 0/1 Knapsack Intuition

## 1. What `dp[j]` Represents
- `dp[j] = true` means: **using the numbers processed so far, there exists a subset whose sum equals exactly `j`.**
- Initially只有空集，所以 `dp[0] = true`，其余为 `false`。

## 2. Why the Double Loop Looks Like This
```cpp
for (int num : nums) {
    for (int j = target; j >= num; --j) {
        dp[j] = dp[j] || dp[j - num];
    }
}
```
1. **Outer loop (每个 num 走一次)**：逐个决定“要不要加入这个数”。
2. **Inner loop倒序 (j = target → num)**：确保每个 `num` 只被使用一次。
   - 如果改成顺序 `j = num → target`，`dp[j - num]` 可能是本轮刚设为 `true` 的值，会导致一个元素被重复使用，退化成完全背包。
3. **更新语义**：
   - `dp[j - num] == true` 表示“之前的某个子集刚好凑到 `j - num`”。
   - 既然我们打算把当前 `num` 放进去，就能凑到 `j`，因此把 `dp[j]` 置 `true`。

## 3. Mental Model
- 想象每个 `num` 是一块积木，`j` 是堆高。
- 倒序遍历意味着：先尝试填高层（接近 target）的空位，避免同一块积木在同一层中被用两次。
- 每一层的布尔值记录“这一层能否被现有积木精确填满”。

## 4. Debug Checklist
- `total` 若为奇数，直接返回 `false`。
- `target = total / 2`。
- `dp` 长度 `target + 1`，并且在进入 outer loop 前设置 `dp[0] = true`。
- 倒序循环的起点是 `target`，终点是 `num`。
- 想象一个小例子（如 `[1,5,11,5]`）打印 `dp` 序列，观察 true 的位置如何扩张。

## 5. 下一步练习
- 重做 416 时先口述上述语义，再写代码。
- 类似题目：1049、494、698（带回溯），练习时都要解释“倒序的原因”。
