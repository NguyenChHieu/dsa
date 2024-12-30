class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        mapping = ['A','T','G','C']
        def change(gene):
            changes = []
            for i in range(len(gene)):
                for c in mapping:
                    mt = gene[:i] + c + gene[i+1:]
                    if mt in bank:
                        changes.append(mt)
            return changes

        q = deque([(startGene, 0)])
        seen = set()
        seen.add(startGene)

        while q:
            g, steps = q.popleft()
            if g == endGene:
                return steps
            mutate = change(g)
            for mg in mutate:
                if mg not in seen:
                    q.append((mg,steps +1))
                    seen.add(mg)
        return -1
