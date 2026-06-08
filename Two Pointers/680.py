class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        s_i = s
        s_j = s
        while(i<j):
            if s[i] != s[j]:
                s_i = s[:i] + s[i+1:]
                s_j = s[:j] + s[j+1:]
                break
            i+=1
            j-=1

        return (s_i[::-1] == s_i or s_j[::-1] == s_j)