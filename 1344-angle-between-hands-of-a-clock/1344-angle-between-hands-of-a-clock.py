class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hrangle=minutes*0.5+(hour%12)*30
        minangle=minutes*6
        angle=abs(hrangle-minangle)
        return min(angle,360-angle)