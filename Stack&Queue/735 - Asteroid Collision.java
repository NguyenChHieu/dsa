class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> save = new Stack();

        int idx = 0;
        while (idx < asteroids.length){
            int curr = asteroids[idx];

            if (save.isEmpty()
                    || save.peek() > 0 && curr > 0
                    || save.peek() < 0 && curr < 0 ){
                save.push(curr);
            }
            else{
                while(!save.isEmpty()
                        // top go right, curr go left to collide
                        && save.peek() > 0 && curr < 0){
                    Integer top = save.peek();

                    // both destroyed
                    if (Math.abs(top) == Math.abs(curr)){
                        save.pop();
                        curr = 0; // curr asteroid destroyed
                        break;
                    }
                    // top gets destroyed, curr remain
                    else if (Math.abs(top) < Math.abs(curr)){
                        save.pop();
                    }
                    // curr gets destroyed, top remain
                    else{
                        curr = 0;
                        break;
                    }
                }
                if (curr != 0){
                    save.push(curr);
                }
            }
            idx++;
        }
        return save.stream().mapToInt(i -> i).toArray();
    }
}