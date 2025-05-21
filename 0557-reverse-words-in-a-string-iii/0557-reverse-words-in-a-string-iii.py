class Solution(object):
    def reverseWords(self, s):
       s1=s.split(' ')
       s=""
       for i in s1:
         s+=i[::-1]+" "
       s=s.strip()
       return s