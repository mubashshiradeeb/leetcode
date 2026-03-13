class Solution(object):
    def hammingWeight(self, n):
        n=bin(n)[2:]
        return len(n.replace("0",""))