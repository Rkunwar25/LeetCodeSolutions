class Solution(object):
    def areNumbersAscending(self, s):
        l=[]
        
        s=s.split(' ')
        for i in s:
            if i.isdigit():
                l.append(float(i))
        if len(list(set(l)))==1:
            return False
        if l==sorted(l)  and len(list(set(l)))==len(l):
            return True
        else:
            return False
        