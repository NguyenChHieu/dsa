class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Since its asking to check a word with freq of ALL of the words in words2
        ,just keep a hashmap that keep mx freq of each char.
        """

        hm = [0] * 26
        for w in words2:
            sub_hm = [0] * 26
            for c in w:
                sub_hm[ord(c) - ord("a")] += 1
            for k in range(26):
                if hm[k] < sub_hm[k]:
                    hm[k] = sub_hm[k]

        ans = []
        for w in words1:
            sub_hm = [0] * 26
            for c in w:
                sub_hm[ord(c) - ord("a")] += 1

            is_valid = True
            for k in range(26):
                if sub_hm[k] < hm[k]:
                    is_valid = False
                    break

            if is_valid:
                ans.append(w)

        return ans
