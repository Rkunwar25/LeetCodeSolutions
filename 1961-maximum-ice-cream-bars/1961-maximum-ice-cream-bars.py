class Solution(object):
    def maxIceCream(self, costs, coins):
        c=0
        costs.sort()
        if coins<costs[0]:
            return 0
        for i in costs:
            if coins==0:
                break
            elif coins>=i:
                coins-=i
                c+=1
        return c