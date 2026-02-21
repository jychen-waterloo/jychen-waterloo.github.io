class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int hi = *max_element(piles.begin(), piles.end());
        int lo = 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            long long hours = 0;
            for (int pile : piles) {
                hours += (pile + mid - 1) / mid; // ceil(pile / mid)
                if (hours > h) break;            // early exit if already too slow
            }
            if (hours > h) {
                lo = mid + 1;    // speed too slow, go faster
            } else {
                hi = mid;        // mid works, try smaller speed in [lo, mid)
            }
        }
        return lo;
    }
};
