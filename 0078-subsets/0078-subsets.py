class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        return list(itertools.chain.from_iterable(itertools.combinations(nums, r) for r in range(len(nums) + 1)))