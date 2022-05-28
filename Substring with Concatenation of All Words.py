# 30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        if not s or not words:
            return result
        word_map = Counter(words)
        word_size = len(words[0])
        num_word = len(words)
        list_size = word_size * num_word
        for i in range(len(s) - list_size + 1):
            seen = dict(word_map)
            word_used = 0
            for j in range(i, i + list_size, word_size):
                sub_str = s[j: j + word_size]
                if sub_str in seen and seen[sub_str] > 0:
                    seen[sub_str] -= 1
                    word_used += 1
                else:
                    break
            if word_used == num_word:
                result.append(i)
        return result