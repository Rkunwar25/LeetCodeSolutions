class Solution(object):
    def findComplement(self, num):
        # b=bin(num)[2:]
        
        # s=''
        # for i in b:
        #     s+='0' if i=='1' else '1'
        # return int(s,2)
        if num == 0:
           return 1  # Special case

        bits = num.bit_length()     # Find number of bits needed
        mask = (1 << bits) - 1       # Create a mask with all bits 1
        return num ^ mask            # XOR num with mask to flip bits
