class Solution(object):
    def calculateTax(self, brackets, income):
        tax = 0.0
        prev = 0  # lower bound of current bracket
        
        for upper, percent in brackets:
            if income <= prev:
                break
            # taxable income in this bracket is min(income, upper) - prev
            taxable = min(income, upper) - prev
            tax += taxable * (percent / 100.0)
            prev = upper  # move to next bracket

        return tax
