class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words = re.findall(r'\w+', paragraph.lower())
        banned_set = set(banned)
        word_count = Counter(word for word in words if word not in banned_set)
        return word_count.most_common(1)[0][0]