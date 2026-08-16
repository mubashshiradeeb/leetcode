class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        b=[]
        a=len(indices)
        for i in range(a):
            b.append(s[indices.index(i)])
        return "".join(b)