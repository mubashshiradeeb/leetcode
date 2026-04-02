class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num)
        greatest=s
        for digit in s:
            if digit!='9':
                greatest=s.replace(digit, '9')
                break
        smallest=s.replace(s[0], '0')
        return int(greatest)-int(smallest)