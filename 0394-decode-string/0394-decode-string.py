class Solution(object):
  def decodeString(self,s: str) -> str:
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push the current string and number to stack and reset them
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            # Pop the last string and number, and repeat current string
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            # It's a character, just add it to current string
            current_str += char

    return current_str
