class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        b=""
        a=len(indices)
        for i in range(a):
            b+=s[indices.index(i)]
        return b