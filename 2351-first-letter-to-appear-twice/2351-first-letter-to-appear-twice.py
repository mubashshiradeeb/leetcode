class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        for i in s:
            if i not in a:
                a+=i
            else:
                return i