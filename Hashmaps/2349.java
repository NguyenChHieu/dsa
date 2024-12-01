import java.util.HashMap;
import java.util.Set;
import java.util.TreeSet;

class NumberContainers {
    private HashMap<Integer, Set<Integer>> save;
    private HashMap<Integer,Integer> container;

    public NumberContainers() {
        container = new HashMap<>();
        save = new HashMap<>();
    }

    public void change(int index, int number) {
        if (container.containsKey(index)){
            int oldNumber = container.get(index);
            container.put(index, number);

            var set = save.get(oldNumber);
            set.remove(index);

            var newSet = save.getOrDefault(number, new TreeSet<>());
            newSet.add(index);
            save.put(number, newSet);
        }
        else{
            container.put(index, number);
            var newSet = save.getOrDefault(number, new TreeSet<>());
            newSet.add(index);
            save.put(number, newSet);
        }
    }

    public int find(int number) {
        if (save.containsKey(number)){
            if (save.get(number).isEmpty()){
                return -1;
            }
            else{
                return save.get(number).iterator().next();
            }
        }
        else return -1;
    }
}