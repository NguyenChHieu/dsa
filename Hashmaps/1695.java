class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int l = 0;
        int r = 0;

        HashSet<Integer> save =  new HashSet<>();
        int ans = 0;
        int curr = 0;

        while (r < nums.length){
            if (save.contains(nums[r])){
                while (save.contains(nums[r])){
                    save.remove(nums[l]);
                    curr -= nums[l];
                    l++;
                }
            }
            save.add(nums[r]);
            curr += nums[r];
            ans = Math.max(ans, curr);
            r++;
        }
        return ans;
    }
}