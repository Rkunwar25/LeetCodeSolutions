from collections import Counter

class Solution(object):
    def findEvenNumbers(self, digits):
        digit_count = Counter(digits)
        result = []

        for num in range(100, 1000, 2):  # even 3-digit numbers
            num_digits = [int(d) for d in str(num)]
            num_count = Counter(num_digits)
            if all(num_count[d] <= digit_count[d] for d in num_count):
                result.append(num)

        return result
