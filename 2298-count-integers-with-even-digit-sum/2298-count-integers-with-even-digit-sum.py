class Solution(object):
    def countEven(self, num):
        def digSum(n):
            s=0
            for i in str(n):
                s+=int(i)
            return s
        c=0
        for i in range(1,num+1):
            if digSum(i)%2==0:
                c+=1
        return c