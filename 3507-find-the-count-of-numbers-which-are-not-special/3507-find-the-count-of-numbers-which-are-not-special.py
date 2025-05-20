class Solution(object):
    def nonSpecialCount(self, l, r):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        count_special = 0
        start = int(math.ceil(l**0.5))
        end = int(math.floor(r**0.5))

        for i in range(start, end + 1):
            if is_prime(i):
                sq = i * i
                if l <= sq <= r:
                    count_special += 1

        total = r - l + 1
        return total - count_special
