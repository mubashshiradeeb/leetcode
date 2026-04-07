class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=" "
        for i in s:
            if stack[-1]==i:
                stack=stack[:-1]
            else:
                stack+=i
        return stack[1:]