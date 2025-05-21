class Solution(object):
    def backspaceCompare(self, s, t):
      def build(string):
        result = []
        for char in string:
            if char == '#':
                if result:
                    result.pop()
            else:
                result.append(char)
        return result
        
      return build(s)==build(t)