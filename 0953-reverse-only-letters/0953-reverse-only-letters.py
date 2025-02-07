class Solution(object):
    def reverseOnlyLetters(self, s):
        letter=[]
        for i in list(s):
            if i.isalpha():
                letter.append(i)
        letter.reverse()
        j=0
        s1=""
        for i in range(len(s)):
            if s[i].isalpha():
                s1+=letter[j]
                j+=1
            else:
                s1+=s[i]
        return s1