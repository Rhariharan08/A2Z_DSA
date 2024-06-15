# https://leetcode.com/problems/fruit-into-baskets/description/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = maxlen = 0
        basket = defaultdict(int)
        while r < len(fruits):
            basket[fruits[r]] = basket.get(fruits[r], 0)+1

            if len(basket)>2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
            if len(basket)<=2:
                maxlen = max(maxlen, r-l+1)
            r += 1
        
        return maxlen
      
