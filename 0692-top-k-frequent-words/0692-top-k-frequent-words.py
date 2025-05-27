class Solution(object):
    def topKFrequent(self, words, k):
        c=Counter(words)
        l=[]
        lc=sorted(c.items(),key=lambda x:(-x[1],x[0]))
        count=0
        for i,j in lc:
            if count==k:
                break
            l.append(i)
            count+=1
        return l