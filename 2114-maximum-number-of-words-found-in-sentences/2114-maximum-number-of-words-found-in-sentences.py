class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        b=0
        for i in sentences:
            a=i.count(" ")
            if a>b:
                b=a
        return b+1