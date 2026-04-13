class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        a=[]
        for i in nums:
            sum+=i
            a.append(sum)
        return a