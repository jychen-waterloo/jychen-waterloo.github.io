# Minimum Size Subarray Sum Notes

- Maintain a running `sum` for the window; never mutate the `target` argument itself or you'll lose clarity about what the loop checks.
- Shrink condition must be `while (sum >= target)` because any window whose total already meets the requirement can potentially be shortened.
- Update the answer **before** subtracting `nums[left]`, so the current window length is recorded before the left bound moves.
- Template reminder:
  ```cpp
  int minSubArrayLen(int target, vector<int>& nums) {
      int left = 0, sum = 0, best = nums.size() + 1;
      for (int right = 0; right < nums.size(); ++right) {
          sum += nums[right];
          while (sum >= target) {
              best = min(best, right - left + 1);
              sum -= nums[left++];
          }
      }
      return best == nums.size() + 1 ? 0 : best;
  }
  ```
