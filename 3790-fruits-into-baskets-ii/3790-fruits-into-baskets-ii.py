class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n=len(fruits)
        for i in range(n):
            for j in range(n):
                if fruits[i]<=baskets[j]:
                    baskets[j]=0
                    break
        baskets=[x for x in baskets if x != 0]
        return len(baskets)