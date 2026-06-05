class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        l = len(strs)
        strs.sort()
        pre= strs[0]
        
        for i in range(1, l):
            l0 = len(pre)
            for j in range(l0):
                if j < len(strs[i]):
                    if pre[j] != strs[i][j]:
                        pre = pre[:j]
                        break
                else:
                    pre = pre[:j]
                    break
        
        return pre



