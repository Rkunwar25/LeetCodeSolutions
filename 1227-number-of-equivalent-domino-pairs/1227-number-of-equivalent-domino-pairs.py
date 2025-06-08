class Solution(object):
    def numEquivDominoPairs(self, dominoes):
       l=[]
       for i in dominoes:
          l.append(sorted(i))
       l=[tuple(i) for i in l]
       c=Counter(l)
       count=0
       for i in c.values():
         if i>1:
            count+=i*(i-1)//2
       return count