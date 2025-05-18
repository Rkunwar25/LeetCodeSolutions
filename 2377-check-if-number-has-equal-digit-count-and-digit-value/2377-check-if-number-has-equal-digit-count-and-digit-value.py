class Solution(object):
    def digitCount(self, num):
        
        for i in range(len(num)):
            if num.count(str(i))!=int(num[i]):
                return False
        return True