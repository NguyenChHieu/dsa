class Solution {
    public String predictPartyVictory(String senate) {
        // keep 2 queues of each team, then let the "front" fight, the lower index will be pop
        // the winner gets pushed to back.

        Queue<Integer> rad = new LinkedList<Integer>();
        Queue<Integer> dir = new LinkedList<Integer>();

        // setup both queues
        int i = 0;
        for (char c: senate.toCharArray()){
            if (c == 'R'){
                rad.offer(i);
            }
            else dir.offer(i);
            i++;
        }

        int sze =senate.length();

        while (!rad.isEmpty() && !dir.isEmpty()){
            if (rad.peek() < dir.peek()){
                dir.poll();
                rad.poll();
                rad.offer(sze++);
            }
            else{
                dir.poll();
                rad.poll();
                dir.offer(sze++);
            }
        }

        if (rad.isEmpty()){
            return "Dire";
        } else return "Radiant";
    }
}