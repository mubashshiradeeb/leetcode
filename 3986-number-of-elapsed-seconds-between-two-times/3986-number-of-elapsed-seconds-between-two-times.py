class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        hsecond1=int(startTime[:2])*3600
        msecond1=int(startTime[3:5])*60
        seconds1=int(startTime[6:])
        hsecond2=int(endTime[:2])*3600
        msecond2=int(endTime[3:5])*60
        seconds2=int(endTime[6:])
        return (hsecond2+msecond2+seconds2)-(hsecond1+msecond1+seconds1)
