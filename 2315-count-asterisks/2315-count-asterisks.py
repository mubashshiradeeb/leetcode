class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        a=[]
        for i in s:
            if i=="|":
                count+=1
            if count%2==0:
                a.append(i)
        return a.count("*")