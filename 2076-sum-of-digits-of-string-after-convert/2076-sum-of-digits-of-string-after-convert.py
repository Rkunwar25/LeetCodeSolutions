class Solution(object):
    def getLucky(self, s, k):
        def ano(char):
            return ord(char.lower()) - ord('a') + 1
        def sumDig(n):
            n=str(n)
            s=0
            for i in n:
                s+=int(i)
            return s
        c=0
        sn=""
        for i in s:
            sn+=str(ano(i))
        sn=int(sn)
        while c<k:
            sn=sumDig(sn)
            c+=1
        return sn