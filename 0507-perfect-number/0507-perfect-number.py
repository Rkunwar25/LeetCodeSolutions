class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        sum1=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sum1+=i
                if i!=num//i:
                    sum1+=num//i
        if sum1==num:
            return True
        else:
            return False