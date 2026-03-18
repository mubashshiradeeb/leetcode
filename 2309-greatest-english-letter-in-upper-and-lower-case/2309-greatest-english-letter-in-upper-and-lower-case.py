class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in s:
            if i in alpha:
                a+=i
        a="".join(sorted(a))[::-1]
        for i in a:
            if i.lower() in s:
                return i
        return ""