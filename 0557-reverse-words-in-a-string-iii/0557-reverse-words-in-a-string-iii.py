class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        result=[]
        for word in s:
            r_word = word[::-1]
            result.append(r_word)
        return " ".join(result)