# LeetCode Practice Pool

Use this list to track Jiayi's must-practice problems. Update the table whenever a problem is attempted so we can see repetition counts, last touch dates, and current mastery confidence levels.

> Date convention: study-day interpretation follows **America/Toronto**. Raw system timestamps may be UTC, but daily progress reviews should use Toronto local date.

## Mastery Scale
- **Learning** – still figuring out the core idea or pattern.
- **Warming Up** – can solve with light hints or after a reminder.
- **Comfortable** – can solve independently within target time.
- **Mastered** – fluent, can teach/explain variants.

## Problem Pool
| # | Title | Core Topic(s) | Difficulty | Attempts | Last Attempt | Mastery | Notes |
|---|-------|----------------|------------|----------|--------------|---------|-------|
| 1 | Two Sum | hash map, array | Easy | 1 | 2025-12-27 | Comfortable | 使用哈希表存储已遍历过的数字及其索引，遍历数组时检查目标值与当前值的差是否在哈希表中，时间复杂度O(n)。 |
| 2 | Add Two Numbers | linked list | Medium | 1 | 2026-01-02 | Comfortable | 需要考虑进位问题。 |
| 3 | Longest Substring Without Repeating Characters | two pointers, hash map, array, sliding window | Medium | 1 | 2025-12-29 | Warming Up | 使用bool[256]代替哈希表，双指针维护窗口。 |
| 11 | Container With Most Water | two pointers, greedy | Medium | 1 | 2025-12-28 | Comfortable | 移动较短的边才可能增大面积。 |
| 15 | 3Sum | two pointers, array | Medium | 1 | 2025-12-28 | Warming Up | 排序后双指针求2-sum并去重。 |
| 19 | Remove Nth Node From End of List | two pointers, linked list | Medium | 1 | 2025-12-30 | Warming Up | 快指针先走n步后与慢指针同速前进。 |
| 20 | Valid Parentheses | string, stack | Easy | 1 | 2026-01-03 | Comfortable | 经典栈匹配题。 |
| 21 | Merge Two Sorted Lists | two pointers, array | Easy | 1 | 2025-12-30 | Comfortable | 哨兵节点合并并释放。 |
| 23 | Merge k Sorted Lists | priority queue, array, linked list | Hard | 1 | 2026-01-10 | Warming Up | 用k大小最小堆维护头节点，O(k)空间。 |
| 33 | Search in Rotated Sorted Array | binary search | Medium | 3 | 2026-02-21 | Learning | 6 分钟复习，重点记录 `>=` 判断的理由；再刷几次把有序半区判断写成肌肉记忆。 |
| 34 | Find First and Last Position of Element in Sorted Array | binary search | Medium | 3 | 2026-02-25 | Learning | 今日 23 分钟、4 次提交后 AC；边界易错，列为重点复习题，固定使用 `[l,r)` + lower/upper 模板；本轮 11 分钟，2 次提交 AC。 |
| 46 | Permutations | backtracking | Medium | 1 | 2026-01-06 | Warming Up | 标准回溯，需要熟练。 |
| 48 | Rotate Image | array | Medium | 2 | 2026-02-19 | Warming Up | 本轮11分钟无提示完成，按分层四元旋转；可再熟练直接转置+反转写法。 |
| 49 | Group Anagrams | hash map, string | Medium | 1 | 2025-12-29 | Warming Up | 按排序串或字符频率作为hash键。 |
| 53 | Maximum Subarray | divide & conquer, dynamic programming, array | Medium | 1 | 2026-01-31 | Learning | DP压缩可得Kadane算法。 |
| 54 | Spiral Matrix | array | Medium | 1 | 2026-02-08 | Learning | 按m*n遍历，碰壁转向。 |
| 55 | Jump Game | greedy | Medium | 2 | 2026-02-16 | Comfortable | 4 min 无提示，最远可达贪心模板熟练。 |
| 56 | Merge Intervals | array | Medium | 1 | 2026-01-18 | Comfortable | 排序后顺序合并。 |
| 70 | Climbing Stairs | dynamic programming | Easy | 1 | 2026-01-17 | Comfortable | 等价斐波那契。 |
| 73 | Set Matrix Zeroes | array | Medium | 1 | 2026-02-08 | Warming Up | 用首行首列做零标记实现O(1)空间。 |
| 76 | Minimum Window Substring | two pointers | Hard | 4 | 2026-02-21 | Warming Up | count 可为负、missing==0 才收缩这套逻辑已稳定；继续保持每次 shrink 前先更新答案。 |
| 77 | Combinations | backtracking | Medium | 1 | 2026-01-06 | Warming Up | 标准回溯。 |
| 78 | Subsets | bitmap, backtracking | Medium | 1 | 2026-01-06 | Comfortable | 可用回溯或位掩码。 |
| 81 | Search in Rotated Sorted Array II | binary search | Medium | 3 | 2026-03-01 | Learning | 12 分钟、2 次提交 AC；关键是 `left==mid==right` 时先去重（`left++/right--`）再判有序半区；二刷 5 分钟 1 次 AC；本轮 4 分钟，2 次 AC。 |
| 88 | Merge Sorted Array | two pointers | Easy | 1 | 2025-12-27 | Warming Up | 双指针从后往前可避免额外空间。 |
| 98 | Validate Binary Search Tree | tree, DFS | Medium | 1 | 2026-01-05 | Comfortable | 注意上下界和溢出。 |
| 100 | Same Tree | BFS, tree | Easy | 1 | 2026-01-04 | Comfortable | DFS递归比较左右子树。 |
| 102 | Binary Tree Level Order Traversal | tree, DFS | Medium | 2 | 2026-02-20 | Comfortable | 7 分钟 BFS 模板一次写完，可考虑再练 DFS 版本。 |
| 104 | Maximum Depth of Binary Tree | tree | Easy | 1 | 2026-01-04 | Comfortable | 经典递归。 |
| 121 | Best Time to Buy and Sell Stock | two pointers | Easy | 1 | 2026-02-01 | Comfortable | 维护最低买价与后续卖价。 |
| 125 | Valid Palindrome | two pointers, string | Easy | 1 | 2026-02-01 | Comfortable | 字母数字都要考虑。 |
| 128 | Longest Consecutive Sequence | Union-Find, array | Medium | 1 | 2026-01-17 | Learning | 用unordered_set找序列头确保O(n)。 |
| 133 | Clone Graph | hash map, DFS | Medium | 1 | 2026-01-11 | Comfortable | DFS+哈希表缓存节点。 |
| 141 | Linked List Cycle | two pointers, linked list | Easy | 1 | 2025-12-30 | Comfortable | Floyd判环。 |
| 143 | Reorder List | two pointers, linked list | Medium | 1 | 2026-01-02 | Warming Up | 快慢指针找中点，反转后交替合并。 |
| 155 | Min Stack | stack | Medium | 1 | 2026-01-03 | Warming Up | 双栈跟踪最小值。 |
| 160 | Intersection of Two Linked Lists | two pointers, linked list | Easy | 1 | 2026-01-02 | Comfortable | 双指针遍历两次相遇。 |
| 169 | Majority Element | array | Easy | 1 | 2026-02-01 | Comfortable | Boyer-Moore投票法。 |
| 189 | Rotate Array | two pointers, array | Medium | 1 | 2026-02-02 | Learning | 反转三次即可原地旋转。 |
| 198 | House Robber | dynamic programming | Medium | 2 | 2026-02-19 | Warming Up | 5分钟完成，滚动 rob/skip 状态写法熟练，可再练变体 House Robber II。 |
| 200 | Number of Islands | DFS | Medium | 1 | 2026-01-11 | Comfortable | DFS染色统计岛屿。 |
| 206 | Reverse Linked List | linked list | Easy | 1 | 2025-12-30 | Comfortable | 迭代反转指针。 |
| 207 | Course Schedule | BFS, DFS | Medium | 1 | 2026-01-17 | Warming Up | Kahn算法：入度数组+队列。 |
| 209 | Minimum Size Subarray Sum | two pointers, array, sliding window | Medium | 3 | 2026-02-21 | Learning | 6 min 完成但一度写成 `sum==target`；笔记中强调用独立 sum 并在 `sum>=target` 时收缩。 |
| 210 | Course Schedule II | graph, topological-sort, bfs | Medium | 1 | 2026-03-01 | Learning | 7 分钟，1 次 AC；沿用 Kahn 拓扑排序输出顺序，最终通过 `order.size()==numCourses` 校验有无环。 |
| 213 | House Robber II | dynamic programming | Medium | 1 | 2026-02-21 | Learning | 环形版本拆成 `rob(0..n-2)` 与 `rob(1..n-1)` 两段线性，18 分钟一次 AC。 |
| 215 | Kth Largest Element in an Array | QuickSelect, priority queue, divide & conquer, array | Medium | 1 | 2026-01-10 | Warming Up | 最小堆或QuickSelect。 |
| 217 | Contains Duplicate | hash map, array | Easy | 1 | 2025-12-27 | Comfortable | 用unordered_set检测重复。 |
| 226 | Invert Binary Tree | tree | Easy | 1 | 2026-01-04 | Comfortable | 递归交换左右子树。 |
| 230 | Kth Smallest Element in a BST | inorder traversal, tree | Medium | 1 | 2026-01-05 | Warming Up | 迭代中序遍历。 |
| 235 | Lowest Common Ancestor of a BST | BST | Easy | 1 | 2026-01-05 | Comfortable | 利用BST大小关系定位。 |
| 238 | Product of Array Except Self | prefix product, array | Medium | 2 | 2026-02-20 | Comfortable | 两遍前缀乘法模板熟练，能在 6 分钟内完成。 |
| 242 | Valid Anagram | hash map, string | Easy | 1 | 2025-12-27 | Comfortable | 统计字符频率。 |
| 283 | Move Zeroes | two pointers, array | Easy | 2 | 2026-02-19 | Warming Up | 2分半完成，使用写指针先收集非零再统一补零，逻辑清晰。 |
| 300 | Longest Increasing Subsequence | dynamic programming | Medium | 2 | 2026-02-17 | Warming Up | 9 min，依赖记忆的 patience / lower_bound 模板完成；需要再理解为何 dp 保存的是“长度k的最小尾值”。 |
| 322 | Coin Change | dynamic programming | Medium | 1 | 2026-01-18 | Warming Up | 经典dp：dp[amount]。 |
| 347 | Top K Frequent Elements | priority queue, hash map, array | Medium | 1 | 2026-01-10 | Warming Up | 频率统计+最小堆或桶排序。 |
| 416 | Partition Equal Subset Sum | dynamic programming | Medium | 2 | 2026-02-21 | Learning | 今天 7 分钟凭记忆完成 0/1 背包模板，但倒序更新 / dp[j] 含义仍需巩固。 |
| 417 | Pacific Atlantic Water Flow | DFS | Medium | 1 | 2026-01-11 | Warming Up | 从两侧分别DFS取交集。 |
| 424 | Longest Repeating Character Replacement | two pointers, array, sliding window | Medium | 1 | 2026-02-10 | Warming Up | maxFreq只需记录最大值。 |
| 438 | Find All Anagrams in a String | two pointers, string, sliding window | Medium | 2 | 2026-02-16 | Comfortable | 4 min 无提示二刷成功；固定窗口+missing 模板已经稳定。 |
| 494 | Target Sum | dynamic programming, 0-1-knapsack | Medium | 3 | 2026-03-01 | Learning | 16 分钟、2 次提交 AC；已掌握转化为 `(sum+target)/2` 子集计数，需牢记先判 `sum+target>=0` 且为偶数；二刷 7 分钟 2 次 AC；本轮 8 分钟，1 次 AC。 |
| 560 | Subarray Sum Equals K | prefix sum | Medium | 4 | 2026-02-25 | Learning | 5 min 一次过，顺序牢记“查 prefix-k → 累加结果 → map[prefix]++”；注意结果可能要用 long long；本轮 12 分钟，1 次提交 AC。 |
| 567 | Permutation in String | two pointers, hash map, sliding window | Medium | 1 | 2025-12-29 | Warming Up | int[26]统计频率，滑动窗口检查。 |
| 739 | Daily Temperatures | monotonic stack, stack | Medium | 1 | 2026-01-03 | Warming Up | 逆向更高效，遇升温出栈。 |
| 875 | Koko Eating Bananas | binary search | Medium | 3 | 2026-03-01 | Learning | 记录了 `[lo, hi)` 模板与 `hi=mid` 的理由；二刷 6 分钟 1 次 AC；本轮 4 分钟，1 次 AC。 |
| 840 | Magic Squares In Grid | sliding window | Medium | 1 | 2025-12-29 | Comfortable | 中心必须是5，行列和为15且无重复。 |
| 1351 | Count Negative Numbers in a Sorted Matrix | two pointers | Easy | 1 | 2025-12-28 | Comfortable | 从左下走向右上，根据符号移动。 |
| 2402 | Meeting Rooms III | priority queue, greedy | Hard | 1 | 2025-12-27 | Warming Up | 两个最小堆跟踪空房与占用房。 |

## Next Additions
- Mirror any new Notion entries here as soon as they are marked「重点学习」or「初次学习」so the schedule stays synced.
- Add classic problems per topic focus (e.g., binary search, tree traversals) once they appear in regular rotations.
- When a new problem becomes "must review", append it with Attempts=0 and Mastery=Learning, then update after each session.

## Update Process
1. Log each session in `leetcode/ledger.jsonl` as usual.
2. Mirror must-review problems here with cumulative attempt counts.
3. Revisit problems tagged "Learning/Warming Up" within 3–5 days.
