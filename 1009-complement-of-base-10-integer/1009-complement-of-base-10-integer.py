class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=str(bin(n))[2:]
        b=""
        for i in a:
            if i=="0":
                b+="1"
            if i=="1":
                b+="0"
        return int(b,2)