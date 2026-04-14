class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        import numpy as np
        arr.sort()
        a=len(arr)//20
        b=arr[a:-a]
        return np.mean(b)