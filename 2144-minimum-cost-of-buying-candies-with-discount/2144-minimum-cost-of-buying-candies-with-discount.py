class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<3:
            return sum(cost)
        cost.sort(reverse=True)
        costsum=0
        for i in range(0,len(cost),3):
            costsum+=cost[i]
            if i+1<len(cost):
                costsum+=cost[i+1]
        return costsum