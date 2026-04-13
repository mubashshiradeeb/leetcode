class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a=list(set(arr))
        b=len(arr)//4
        for i in a:
            if arr.count(i)>b:
                return i