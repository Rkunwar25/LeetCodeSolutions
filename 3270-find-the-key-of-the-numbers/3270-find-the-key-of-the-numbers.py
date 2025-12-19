class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1=str(num1)
        num2=str(num2)
        num3=str(num3)
        if len(num1)<4:
            num1="0"*(4-len(num1))+num1
        if len(num2)<4:
            num2="0"*(4-len(num2))+num2
        if len(num3)<4:
            num3="0"*(4-len(num3))+num3
        s=""
        for i in range(4):
            s+=min(num1[i],num2[i],num3[i])
        return int(s)