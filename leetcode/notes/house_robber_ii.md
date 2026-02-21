# House Robber II Notes

- The circle constraint means the first and last houses cannot both be robbed. Split the problem into two linear passes:
  1. Rob houses in `[0, n-2]` (include first, exclude last).
  2. Rob houses in `[1, n-1]` (exclude first, include last).
- Reuse the linear DP `rob` helper: maintain `take` (rob current) and `skip` (best without current). For each house:
  ```cpp
  long long newTake = skip + nums[i];
  skip = max(skip, take);
  take = newTake;
  ```
- Result for a segment is `max(take, skip)`; final answer is the max of the two segment results.
- Edge cases: if `n == 1`, just return `nums[0]`.
