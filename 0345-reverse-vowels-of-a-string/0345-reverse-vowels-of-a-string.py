class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        vow="aeiouAEIOU"
        for i in s:
            if i in vow:
                a+=i
        a=a[::-1]
        z=0
        b=""
        for i in s:
            if i in vow:
                b+=a[z]
                z+=1
            else:
                b+=i
        return b