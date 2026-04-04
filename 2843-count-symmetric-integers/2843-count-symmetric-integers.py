class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        for i in range(low,high+1):
            i=str(i)
            if len(i)==2:
                if int(i[0])==int(i[1]):
                    count+=1
            elif len(i)==4:
                if int(i[0])+int(i[1])==int(i[2])+int(i[3]):
                    count+=1
        return count