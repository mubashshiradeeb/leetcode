class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        a=moves.count("_")
        b=moves.count("L")
        c=moves.count("R")
        if b>c:
            return a+b-c
        else:
            return a+c-b