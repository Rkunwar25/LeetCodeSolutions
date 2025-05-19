class Solution(object):
    def secondHighest(self, s):
       l=[]
       for i in s:
        if i in "0123456789":
            l.append(int(i))
       st=list(set(l))
       st.sort(reverse=True)
       
       if len(st)>=2:
            return st[1]
       else:
            return -1