class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter in s:
            a=len(s)
            b=s.count(letter)
            return b*100//a
        return 0
        