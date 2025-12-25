class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_count = 0


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = TrieNode()
        ans = 0

        for word in words:
            node = root
            n = len(word)

            # Traverse prefix
            for i in range(n):
                ch = word[i]
                if ch not in node.children:
                    break
                node = node.children[ch]

                # prefix found, now check suffix
                if node.end_count > 0 and word[:i+1] == word[n-i-1:]:
                    ans += node.end_count

            # Insert word into trie
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end_count += 1

        return ans
