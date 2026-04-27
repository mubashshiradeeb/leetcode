class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        leftSum=0
        rightSum=sum(nums)
        for i in nums:
            leftSum+=i
            a.append(abs(leftSum-rightSum))
            rightSum-=i
        return a