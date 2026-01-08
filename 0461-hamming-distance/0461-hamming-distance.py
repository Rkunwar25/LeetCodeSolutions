class Solution(object):
    def hammingDistance(self, x, y):
        # x=bin(x)[2:]
        # y=bin(y)[2:]
        # if len(x)<len(y):
        #     x='0'*(len(y)-len(x))+x
        # elif len(x)>len(y):
        #     y='0'*(len(x)-len(y))+y
        # hd=0
        # for i in range(len(x)):
        #     if x[i]!=y[i]:
        #         hd+=1
        # return hd
                return bin(x ^ y).count('1')
