class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        a=""
        for i in words:
            a+=i[0]
        return a==s