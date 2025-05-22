class Solution(object):
    def average(self, salary):
        salary.sort()
        salary.pop()
        salary.pop(0)
        return float(sum(salary))/len(salary)