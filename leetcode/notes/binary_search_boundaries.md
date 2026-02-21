# Binary Search Boundary Choices · 二分边界选择

> Last updated: 2026-02-21 · Jiayi boundary notes

## 1. Interval conventions / 区间约定

Binary search code stays sane only when the loop invariant (what `l` / `r` mean) is stated explicitly. Two common styles:

| Style | Range meaning | Typical loop | Mid calc | Shrink rules | Finished state |
|-------|---------------|--------------|----------|--------------|----------------|
| **Closed interval** | `[l, r]` 都可行 | `while (l <= r)` | `mid = l + (r-l)/2` | `mid` 不满足时，把它排除：`r = mid - 1` 或 `l = mid + 1` | `l > r` after loop | 
| **Half-open interval** | `[l, r)` 右端不可取 | `while (l < r)` | `mid = l + (r-l)/2` | 若砍右半：`r = mid`; 若砍左半：`l = mid + 1` | `l == r` after loop |

> 记忆法：闭区间 -> `<=` 循环；半开区间 -> `<` 循环。不要混搭，否则“落点”含义会乱。

## 2. 为什么有时要写 `>=` / `<=`

拿「Search in Rotated Sorted Array」举例。

### `if (nums[mid] >= nums[left])` 的原因

- 我们想判断 `[left, mid]` 是否严格有序（即没有跨过旋转点）。
- 当数组刚好没旋转或 `left == mid`（区间长度为 1）时，`nums[mid] == nums[left]`。此时我们仍然要把左半区视为“有序”，否则代码会误以为左边无序，导致去右边继续判断，最终错过目标。
- 使用 `>=` 能覆盖这些边界情况。而 `>` 在 `left == mid` 或者出现重复值时会把左区间判成“无序”（即便原版题目没有重复值，保留 `>=` 可以提高复用性）。

> 中文记忆：当你要把“单元素区间”或“全部相等”的情形也视为有序，就要让条件包含等号。

### 区间内进一步比较时的等号

判断目标是否落在左半区：`if (target >= nums[left] && target < nums[mid])`。

- 左端加 `>=`：因为我们本身在闭区间 `[left, mid]` 内操作，左端包含在内。
- 右端用 `<`：用半开 `[left, mid)`，这样一旦 `target == nums[mid]`，前面的“命中直接返回”分支已经处理，不需要在这里重复考虑；同时保证 `mid` 不会被再次包含进右半搜索，避免死循环。

## 3. `while (left <= right)` vs `while (left < right)`

### 用闭区间 `[left, right]`

- 典型例子：寻找一个确切值或最左/最右满足条件的位置并且习惯返回 index。
- 循环条件 `left <= right`，因为当 `left == right` 时该位置仍需要检查。
- 退出后 `left == right + 1`，表示所有候选都检查完。

### 用半开区间 `[left, right)`

- 常见于「lower_bound / upper_bound」模板或答案空间二分（如 Koko）。
- 不需要额外防溢出：因为 `right` 本来就指向“不可取”位置，某些情况下可以直接设为 `n`。
- 循环 `left < right`，结束后 `left == right` 指向第一个满足条件的位置。

> 快速判断：
> - 需要返回“界限” → 半开更自然。
> - 确定地检索某个 index 并且每步都要判断 `mid` → 闭区间习惯更顺。

## 4. 实操建议 / Practical checklist

1. **先写注释**说明区间语义：`// search on [l, r]` 或 `// search on [l, r)`。
2. 若用闭区间：
   - while 写 `l <= r`；
   - 左半保留 `mid - 1`，右半保留 `mid + 1`；
   - 注意返回值如果是 `l` 或 `r` 要在循环外判断是否越界。
3. 若用半开区间：
   - while 写 `l < r`；
   - 砍右半区时 `r = mid`（不能 `mid - 1`）；砍左半区时 `l = mid + 1`；
   - 返回时 `l` 就是答案（或 `l == n` 表示不存在）。
4. **比较条件带不带等号？**问自己：
   - 这个区间端点是否仍属于“有效候选”？
   - 是否需要让一侧包含等号来避免漏掉单元素？
   - 如果 `mid` 已经被判断过，接下来要不要把它排除掉？（若要排除，使用 `<` / `>` 让它只属于一侧。）

精髓就是：每个 `<=` / `<` 都对应某个不变式。写之前先把不变式说出口，再落到代码里，自然就知道该不该加等号了。
