class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts=Counter(s)
        for index,char in enumerate(s):
            if counts[char]==1:
                return index
        return -1