# Last updated: 08/02/2026, 14:28:00
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, r = 0, len(products) - 1
        res = []

        for i, c in enumerate(searchWord):
            while l <= r and (len(products[l]) <= i or c != products[l][i] ):
                l += 1
            while l <= r and (len(products[r]) <= i or c != products[r][i]):
                r -= 1
            
            remain = min(3, r - l + 1)
            cur_words = []
            for idx in range(remain):
                cur_words.append(products[l + idx])
            res.append(cur_words)
        
        return res


            
        