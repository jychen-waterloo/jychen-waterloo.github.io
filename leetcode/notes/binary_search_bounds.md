# Binary Search Bounds — Lower vs Upper (EN/中文)

## 1. Concept Overview / 概念总览
**English.** `lower_bound` and `upper_bound` are two flavors of binary search over the same sorted array:
- `lower_bound` → first index where `nums[idx] >= target`.
- `upper_bound` → first index where `nums[idx] > target`.
Both allow returning `n` (one past the array) when the target is beyond the existing values.

**中文。** `lower_bound` / `upper_bound` 是同一个排序数组上的两种二分查找：
- `lower_bound`：第一个满足 `nums[idx] >= target` 的位置。
- `upper_bound`：第一个满足 `nums[idx] > target` 的位置。
若目标值落在最大值右侧，二者都会返回 `n`（超出数组一格）。

---

## 2. Implementation Template / 模板代码
```cpp
int lowerBound(const vector<int>& nums, int target) {
    int l = 0, r = nums.size();  // search in [l, r)
    while (l < r) {
        int m = l + (r - l) / 2;
        if (nums[m] < target) {
            l = m + 1;          // target is to the right
        } else {
            r = m;              // nums[m] >= target -> keep m
        }
    }
    return l;                   // may be == nums.size()
}

int upperBound(const vector<int>& nums, int target) {
    int l = 0, r = nums.size();  // search in [l, r)
    while (l < r) {
        int m = l + (r - l) / 2;
        if (nums[m] <= target) {
            l = m + 1;          // still not strictly greater
        } else {
            r = m;
        }
    }
    return l;                   // first index with nums[idx] > target
}
```

**中文提示。**
- `r` 初始设为 `n`，让整个搜索区间是 **左闭右开 `[l, r)`**。
- `while (l < r)` 保证循环结束时 `l == r`，即最小满足条件的下标。
- 两个函数的差别仅在条件：`lower` 用 `< target`，`upper` 用 `<= target`。

---

## 3. Using Them in Range Queries / 套用在区间查询
**English.** To find the first and last position of `target` (LC 34):
1. `start = lowerBound(nums, target)`.
2. If `start == n` or `nums[start] != target`, the target does not exist.
3. Otherwise `end = upperBound(nums, target) - 1` is the last occurrence.

**中文。** 用在“寻找目标的起止位置”时：
1. `start = lowerBound(nums, target)` 找到第一个 `>= target` 的位置。
2. 若 `start == n` 或 `nums[start] != target`，代表数组中没有该值。
3. 否则 `end = upperBound(nums, target) - 1` 即为最后一次出现。

---

## 4. Error Checklist / 常见错误排查
| Pitfall (EN) | Warning Sign | 中文说明 |
|--------------|--------------|----------|
| Mixing closed and half-open intervals | `while (l <= r)` but `r = n` | 右边界设成 `n` 却还用 `<=` 会越界。|
| Forgetting `return n` is valid | For targets larger than every element, result stays at `n-1` | 要让指针有机会走到 `n`，否则无法区分“不存在”。|
| Treating `upper` as “mirror” of `lower` without adjusting the comparison | `t1 >= t2` used to detect failure | `upper` 本来就会返回 `lower + count`，不该用来判定是否找到。|

---

## 5. Practice Checklist / 练习建议
- Rewrite the template twice: once in C++ (above) and once in pseudocode to internalize the interval semantics.
- Dry-run on edge cases: empty array, single element, target smaller than all, greater than all.
- Apply to upcoming binary-search-on-answer problems (Koko Eating Bananas, Search in Rotated Sorted Array) to reinforce the pattern.

**中文。**
- 手写一次模板，确保理解 `[l, r)` 的含义与更新方式。
- 用“空数组 / target 在两端 / target 不存在”做桌面演算，观察指针如何移动。
- 在每次做“答案空间二分”题目前，先回想这份笔记，保持条件判断一致。
