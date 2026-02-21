# Minimum Window Substring Notes

- Maintain two counters: `need` map for required frequencies and `missing` (or `needCount`) for how many characters are still short.
- Expand `right` and decrement `need[s[right]]`; once `need[c]` stays `>= 0`, it means that character satisfied part of the requirement, so decrement `missing`.
- When `missing == 0`, try to shrink from the left:
  1. Update the best answer with the current window.
  2. Increment `need[s[left]]`; if it becomes `> 0`, we just removed a required char, so `missing++` and stop shrinking.
- Using `while (missing == 0)` ensures the window remains valid until we actually remove a critical char.
- Track window boundaries with ints; avoid substr copies until the end.
