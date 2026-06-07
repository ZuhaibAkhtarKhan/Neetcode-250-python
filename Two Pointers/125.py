class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        ns = ""
        for c in s:
            if c.isalnum():
                ns+=c

        s = ns[::-1]
        return s==ns