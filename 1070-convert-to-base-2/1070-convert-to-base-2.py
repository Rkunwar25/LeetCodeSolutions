class Solution(object):
    def baseNeg2(self, n):
        if n == 0:
          return "0"
        res = ""
        while n != 0:
            n, r = divmod(n, -2)
            if r < 0:
              r += 2
              n += 1
            res = str(r) + res
        return res