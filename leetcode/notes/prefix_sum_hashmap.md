# Prefix Sum + Hash Map Checklist (e.g., LC 560)

- Keep a running prefix `sum`. For each index `j`, the number of subarrays ending at `j` with sum `k` is the count of previous prefixes equal to `sum - k`.
- **Order matters:**
  1. Update `sum` with the current number.
  2. Query the map with `sum - k` and add that count to the answer.
  3. Increment the frequency of the current `sum`.
- Initialize the map with `map[0] = 1` so that subarrays starting at index 0 are counted.
- Use `long long` for the answer if array length can be large, since the number of subarrays may overflow 32-bit `int`.
