class Solution(object):
    def checkZeroOnes(self, s):
        s=list(s)
        seq1=0
        seq2=0
        val=0
        for i in s:            
            if int(i) == 1:
                val+=1
                seq1=max(seq1,val)
            else:
                val=0
        val=0
        for i in s:            
            if int(i) == 0:
                val+=1
                seq2=max(seq2,val)
            else:
                val=0
        return seq1>seq2