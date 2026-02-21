# Binary Search Bounds — Lower vs Upper (EN/中文)

## 1. Concept Overview / 觀念總覽
**English.** `lower_bound` and `upper_bound` are two flavors of binary search over the same sorted array:
- `lower_bound` → first index where `nums[idx] >= target`.
- `upper_bound` → first index where `nums[idx] > target`.
Both allow returning `n` (one past the array) when the target is beyond the existing values.

**中文。** `lower_bound` / `upper_bound` 是同一個排序陣列上的兩種二分查找：
- `lower_bound`：第一個滿足 `nums[idx] >= target` 的位置。
- `upper_bound`：第一個滿足 `nums[idx] > target` 的位置。
若目標值落在最大值右側，兩者都會回傳 `n`（超出陣列一格）。

---

## 2. Implementation Template / 樣板程式
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
- `r` 初始設定為 `n`，讓整個搜尋區間是 **左閉右開 `[l, r)`**。
- `while (l < r)` 保證循環結束時 `l == r`，即最小滿足條件的 index。
- 兩個函式的差別僅在條件：`lower` 用 `< target`，`upper` 用 `<= target`。

---

## 3. Using Them in Range Queries / 套用在區間查詢
**English.** To find the first and last position of `target` (LC 34):
1. `start = lowerBound(nums, target)`.
2. If `start == n` or `nums[start] != target`, the target does not exist.
3. Otherwise `end = upperBound(nums, target) - 1` is the last occurrence.

**中文。** 用在「尋找目標的起迄位置」時：
1. `start = lowerBound(nums, target)` 找到第一個 `>= target` 的位置。
2. 若 `start == n` 或 `nums[start] != target`，代表陣列中沒有該值。
3. 否則 `end = upperBound(nums, target) - 1` 即為最後一次出現。

---

## 4. Error Checklist / 常見錯誤排查
| Pitfall (EN) | Warning Sign | 中文說明 |
|--------------|--------------|----------|
| Mixing closed and half-open intervals | `while (l <= r)` but `r = n` | 右邊界設成 `n` 卻還用 `<=` 會越界。|
| Forgetting `return n` is valid | For targets larger than every element, result stays at `n-1` | 要讓指標有機會走到 `n`，否則無法區分「不存在」。|
| Treating `upper` as “mirror” of `lower` without adjusting the comparison | `t1 >= t2` used to detect failure | `upper` 本來就會回傳 `lower+count`，不該用來判斷是否找到。|

---

## 5. Practice Checklist / 練習建議
- Rewrite the template twice: once in C++ (above) and once in pseudocode to internalize the interval semantics.
- Dry-run on edge cases: empty array, single element, target smaller than all, greater than all.
- Apply to upcoming binary-search-on-answer problems (Koko Eating Bananas, Search in Rotated Sorted Array) to reinforce the pattern.

**中文。**
- 手寫一次樣板，確保理解 `[l, r)` 的含義與更新方式。
- 用「空陣列 / target 在兩端 / target 不存在」做桌面演算，觀察指標如何移動。
- 在每次做「答案空間二分」題目前，先回想這份筆記，保持條件判斷一致。
