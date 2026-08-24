class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bums=set(nums)
        a=[]
        for i in range(min(nums),max(nums)):
            if i not in bums:
                a.append(i)
        return a