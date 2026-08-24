class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smallest=min(nums)
        largest=max(nums)
        a=[]
        for i in range(smallest,largest):
            if i not in nums:
                a.append(i)
        return a