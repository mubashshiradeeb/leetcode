class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a=[]
        for i in nums:
            if len(a)<k:
                a.append(i)
            else:
                if i>min(a):
                    a.remove(min(a))
                    a.append(i)
        return a