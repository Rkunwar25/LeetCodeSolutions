class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # Check if the concatenation rule is satisfied
        if str1 + str2 != str2 + str1:
            return ""
        
        # Define GCD function for Python 2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Use the custom GCD function
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the common divisor substring
        return str1[:gcd_length]
