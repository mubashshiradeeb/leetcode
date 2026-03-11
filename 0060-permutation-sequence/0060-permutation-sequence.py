class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from itertools import permutations, islice
        a=list(range(1, n+1))
        a=next(islice(permutations(a),k-1,k))
        return "".join(map(str, a))
        
        