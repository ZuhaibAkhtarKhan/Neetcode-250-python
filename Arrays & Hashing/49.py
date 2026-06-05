class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        '''
        visited = set()
        l = len(strs)
        newS = []

        for i in range(l):
            if len(visited) == len(strs):
                break
            if i not in visited:
                newS.append([strs[i]])
                visited.append(i)
                for j in range(i+1, l):
                    if j not in visited:
                        if sorted(strs[i])== sorted(strs[j]):
                            visited.append(j)
                            newS[-1].append(strs[j])

        return newS
        '''

        anagramMap = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagramMap:
                anagramMap[sorted_s] = []
            anagramMap[sorted_s].append(s)
        return list(anagramMap.values())