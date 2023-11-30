class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return len(s[0])
        words = s.split(" ")
        for word in reversed(words):
            if word != "":
                return len(word)
