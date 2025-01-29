class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        # N+1 since we have n vertices
        # each node is a parent of itself (trivially), so any node havent been processed
        # will return itself as its parent, while also have a rank of 1.
        par = [i for i in range(N+1)] 
        """
        Higher rank = More powerful leader (parent)
        Lower rank = Follower (child in the tree)
        """
        rank = [1] * (N+1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # a edge that has same parent -> a cycle was detected

            # e.g 1-4, find(1) would return 1 (parent of itself), 
            # and since 4 already has a parent which is 1 - marked earlier, find(4) returns 1
            if p1 == p2: 
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]

            else: # khi ma 2 node cung rank - chon cai nao lam bo cung dc nma o day [n1,n2] t chon th n2 lam bo
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]

