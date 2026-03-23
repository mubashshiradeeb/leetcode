class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=""
        num=str(bin(num)[2:])
        for i in num:
            if i=="0":
                a+="1"
            else:
                a+="0"
        return int(a,2)