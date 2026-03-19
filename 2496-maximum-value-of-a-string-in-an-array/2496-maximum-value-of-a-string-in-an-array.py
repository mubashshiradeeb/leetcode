class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        a=[]
        for i in strs:
            if i.isnumeric():
                a.append(int(i))
            else:
                a.append(len(i))
        return max(a)