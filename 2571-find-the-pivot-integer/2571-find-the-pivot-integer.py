class Solution(object):
    def pivotInteger(self, n):
        # l=[i for i in range(n+1)]
        # for i in range(1,len(l)+1):
        #     if sum(l[1:i+1])==sum(l[i:len(l)+1]):
        #         return i
        # return -1
        total = n * (n + 1) // 2
        sqrt_total = int(math.sqrt(total))
        if sqrt_total * sqrt_total == total:
            return sqrt_total
        return -1