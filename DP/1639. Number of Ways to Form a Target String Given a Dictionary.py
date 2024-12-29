class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
        Intuition: precompute all the characters cnt at k-th idx
        in every word. Then, perform memoized backtracking.
        """
        mod = 10 ** 9 + 7
        # (idx, char) among all words, ensure the no char with idx
        # smaller than current idx is used
        cnt = defaultdict(int)
        for w in words:
            for i, c in enumerate(w):
                cnt[(i, c)] += 1

        cache = {}  # (i,k) -> numWays

        # i = target idx, k = idx of words[j][k]
        def dfs(i, k):
            if i == len(target):
                return 1  # a valid way
            if k == len(words[0]):
                return 0  # used up all the chars in the word
            if (i, k) in cache:
                return cache[(i, k)]

            c = target[i]
            # skip the k-th char to check the cases where building the
            # target does not require this k-th char
            cache[(i, k)] = dfs(i, k + 1)
            # instead of redo the computation for the characters that occur
            # multiple times at the same idx, we can just multiply the count.
            # count = cnt[(k, c)] is the number of char c at k-th idx in all words
            if cnt[(k, c)] > 0:
                # dont care about the case where in words array there aren't any char at k-th idx that
                # matches the target char
                cache[(i, k)] += cnt[(k, c)] * dfs(i + 1, k + 1)
            return cache[(i, k)] % mod
        return dfs(0, 0)
        
