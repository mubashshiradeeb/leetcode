class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a,b=nums[0],nums[-1]
        while a:
            b,a=a,b%a
        return b
