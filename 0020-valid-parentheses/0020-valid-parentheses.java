import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            // If it's an opening bracket, push the corresponding closing bracket
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else {
                // If it's a closing bracket
                // Stack empty or top doesn't match → invalid
                if (stack.isEmpty() || stack.pop() != c) {
                    return false;
                }
            }
        }

        // If stack is empty → all brackets matched
        return stack.isEmpty();
    }
}
