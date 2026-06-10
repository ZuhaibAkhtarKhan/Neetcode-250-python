class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        s = "" 
        l1 = len(word1)
        l2 = len(word2)

        i = 0
        while(l1 or l2):
            if(not l1):
                s += word2[i:]
                break
            elif(not l2):
                s+= word1[i:]
                break
            
            s+= word1[i] + word2[i]

            i+=1
            l1-=1
            l2-=1

        return s