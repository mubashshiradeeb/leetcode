class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a=list(set(arr))
        b=[]
        for i in range(len(a)):
            if arr.count(a[i])==a[i]:
                b.append(a[i])
        return b[-1] if b else -1