class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
                return x
        n=x  # Initial guess
        while True:
            new_x = 0.5 * (n + x / n)
            if abs(new_x - n) < 1e-6:  # Convergence check
                 break
            n = new_x
        return int(n)
        