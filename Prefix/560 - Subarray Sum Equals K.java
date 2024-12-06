class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> save = new HashMap<>();
        // by default, sumcurr - k = 0 initialized in hashmap
        save.put(0,1);
        int curr = 0;
        int ans = 0;

        for (int num: nums){
            curr += num;

            // curr_sum - (curr_sum-k) = k
            if (save.containsKey(curr-k)){
                ans += save.get(curr-k);
            }
            save.put(curr, save.getOrDefault(curr, 0)+1);
        }

        return ans;
    }
}