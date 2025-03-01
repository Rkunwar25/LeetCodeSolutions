class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        for i in operations:
            if i[0]=='X' and i[1]=='-' and i[2]=='-':
                X-=1
            elif i[0]=='X' and i[1]=='+' and i[2]=='+':
                X+=1
            elif i[0]=='-' and i[1]=='-' and i[2]=='X':
                X-=1
            elif i[0]=='+' and i[1]=='+' and i[2]=='X':
                X+=1
            
        return X