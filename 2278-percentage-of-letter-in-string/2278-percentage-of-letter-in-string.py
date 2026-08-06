class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        if letter in s:
            a=len(s)
            b=s.count(letter)
            return b*100//a
        return 0