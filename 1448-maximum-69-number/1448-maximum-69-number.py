class Solution(object):
    def maximum69Number (self, num):
        l=[]
        num=str(num)
        for i in range(len(num)):
            l.append(num.replace(num[i],'9',1))
        l.sort(reverse=True)
        return int(l[0])