class Solution:
  def removeKdigits(self,num: str, k: int) -> str:
    stack = []
    
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove remaining digits from the end
    while k > 0:
        stack.pop()
        k -= 1

    # Convert list to string and strip leading zeros
    result = ''.join(stack).lstrip('0')
    
    return result if result else "0"
