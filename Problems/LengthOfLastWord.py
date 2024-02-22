class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = s.strip()[::-1]
        i = 0
        while i < len(r) and r[i] != ' ':
            i += 1
        return i