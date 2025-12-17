# class Solution(object):
#     def checkZeroOnes(self, s):
#         s=list(s)
#         seq1=0
#         seq2=0
#         val=0
#         for i in s:            
#             if int(i) == 1:
#                 val+=1
#                 seq1=max(seq1,val)
#             else:
#                 val=0
#         val=0
#         for i in s:            
#             if int(i) == 0:
#                 val+=1
#                 seq2=max(seq2,val)
#             else:
#                 val=0
#         return seq1>seq2
class Solution(object):
    def checkZeroOnes(self, s):
        max1 = max0 = 0
        count1 = count0 = 0
        
        for ch in s:
            if ch == '1':
                count1 += 1
                max1 = max(max1, count1)
                count0 = 0
            else:
                count0 += 1
                max0 = max(max0, count0)
                count1 = 0
        
        return max1 > max0
