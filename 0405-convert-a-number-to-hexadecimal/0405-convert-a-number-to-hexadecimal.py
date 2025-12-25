class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        res = []
        num &= 0xffffffff
        while num > 0:
            res.append(hex_chars[num & 15])
            num >>= 4
        return "".join(reversed(res))