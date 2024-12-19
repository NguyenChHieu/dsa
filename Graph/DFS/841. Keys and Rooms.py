class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # simply dfs and check if every room is visited.
        seen = set()
        st = [0]

        while st:
            node = st.pop()
            seen.add(node)
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    st.append(neighbor)
        return len(seen) == len(rooms)
