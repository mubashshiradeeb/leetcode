class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=[0]
        alt=0
        for i in gain:
            alt+=i
            a.append(alt)
        return max(a)