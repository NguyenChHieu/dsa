class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic inc
        if len(prices) == 1:
            return prices

        st = []

        for i in range(len(prices)):
            # top > curr thi process top va append.
            while st and st[-1][0] >= prices[i]:
                num, k = st.pop()
                prices[k] = num - prices[i]
            st.append((prices[i], i))

        while st:
            num, k = st.pop()
            prices[k] = num
        return prices
            
