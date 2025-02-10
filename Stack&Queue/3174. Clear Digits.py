class Solution:
    def clearDigits(self, s: str) -> str:
        st = []

        for ch in s:
            if not ch.isdigit():
                st.append(ch)
            else:
                st.pop()
        return "".join(st)
