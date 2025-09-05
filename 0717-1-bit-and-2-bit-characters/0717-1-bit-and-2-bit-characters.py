class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n=len(bits)
        while i < n - 1:   # stop before the last bit
          if bits[i] == 1:
            i += 2
          else:
            i += 1
        return i == len(bits) - 1        