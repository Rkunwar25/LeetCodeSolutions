class Solution(object):
    def countSeniors(self, details):
        c=0
        for i in details:
            if int(i[11:13])>60:
                c+=1
        return c