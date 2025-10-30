class Solution {
    public boolean isPalindrome(String s) {
        char[] str = s.toCharArray();
        int start = 0, end = str.length - 1;

        while (start < end) {
            // skip non-letters/digits
            if (!Character.isLetterOrDigit(str[start])) {
                start++;
            } else if (!Character.isLetterOrDigit(str[end])) {
                end--;
            } else {
                // compare in same case
                if (Character.toUpperCase(str[start]) != Character.toUpperCase(str[end])) {
                    return false;
                }
                start++;
                end--;
            }
        }

        return true;
    }
}
