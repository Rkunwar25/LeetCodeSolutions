class Solution(object):
    def trailingZeroes(self, n):
        # fct=1
        # while(n!=0):
        #     fct*=n
        #     n=n-1
        # s=str(fct)
        # l=list(s)
        # l.reverse()
        # c=0
        # for i in l:
        #     if i=='0':
        #         c+=1
        #     else:
        #         break
        # return c
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count