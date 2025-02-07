# class Solution(object):
#     def reverseOnlyLetters(self, s):
#         letter=[]
#         for i in list(s):
#             if i.isalpha():
#                 letter.append(i)
#         letter.reverse()
#         j=0
#         s1=""
#         for i in range(len(s)):
#             if s[i].isalpha():
#                 s1+=letter[j]
#                 j+=1
#             else:
#                 s1+=s[i]
#         return s1
class Solution(object):
    def reverseOnlyLetters(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        return "".join(s)
