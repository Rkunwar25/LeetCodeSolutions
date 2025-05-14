class Solution(object):
    def halvesAreAlike(self, s):
        s1=s[:len(s)//2]
        s2=s[(len(s)//2):]
        c1,c2=0,0
        for i in s1:
            if i in 'aeiouAEIUO':
                c1+=1
        for i in s2:
            if i in 'aeiouAEIUO':
                c2+=1
        return c1==c2