class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        a=list(set(nums1)|set(nums2)|set(nums3))
        c=[]
        for i in a:
            b=sum([i in nums1, i in nums2, i in nums3])
            if b>=2:
                c.append(i)
        return c