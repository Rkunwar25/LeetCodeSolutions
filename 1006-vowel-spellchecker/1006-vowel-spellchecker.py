class Solution(object):
    def spellchecker(self, wordlist, queries):
        vowels = set('aeiou')

        # Helper function to devowel a word
        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word.lower())

        # --- Preprocessing ---
        exact_words = set(wordlist)  # for exact matches

        # For first-occurrence matches
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_map:
                case_map[lower_word] = word
            dv = devowel(lower_word)
            if dv not in vowel_map:
                vowel_map[dv] = word

        # --- Process each query ---
        result = []
        for q in queries:
            if q in exact_words:
                result.append(q)
            elif q.lower() in case_map:
                result.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:
                result.append(vowel_map[devowel(q)])
            else:
                result.append("")
        return result
