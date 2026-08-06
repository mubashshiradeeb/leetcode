class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        import math
        while 1:
            product=math.prod(int(digit) for digit in str(n))
            if product%t==0:
                return n
            n+=1