class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return True
        num=str(num)
        s=num.strip("0")
        return s==num