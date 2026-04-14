class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans=0
        n=len(mat)
        for i in range(n):
            ans+=mat[i][i]
            ans+=mat[n-i-1][i]
        if n%2!=0:
            ans-=mat[n//2][n//2]
        return ans