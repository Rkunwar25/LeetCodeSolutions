class Solution(object):
    def lexicalOrder(self, n):
       l=[]
       for i in range(1,n+1):
         l.append(str(i))
       l.sort()
       l1=[int(i) for i in l]
       return l1