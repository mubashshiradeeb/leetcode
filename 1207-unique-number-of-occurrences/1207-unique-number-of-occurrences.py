class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        b=[]
        arr1=list(set(arr))
        for i in arr1:
            if arr.count(i) in b:
                return False
            else:
                b.append(arr.count(i))
        return True