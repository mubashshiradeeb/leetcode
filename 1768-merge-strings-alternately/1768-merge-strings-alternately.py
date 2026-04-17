class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a=""
        b=len(word1)
        c=len(word2)
        if b>c:
            for i in range(c):
                a+=word1[i]+word2[i]
            a+=word1[i+1:]
            return a
        else:
            for i in range(b):
                a+=word1[i]+word2[i]
            a+=word2[i+1:]
            return a