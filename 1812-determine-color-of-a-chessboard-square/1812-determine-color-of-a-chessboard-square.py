class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        a="0abcdefgh"
        b=a.index(coordinates[0])
        c=int(coordinates[1])
        if (b+c)%2==0:
            return False
        else:
            return True