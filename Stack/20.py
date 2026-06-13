class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) %2 == 1:
            return False
        
        b = ["(", "[", "{"]
        stack = []

        stack.append(s[0])
        i = 1
        while i < len(s):
            if s[i] in b:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif (s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
            i+=1
        return len(stack) == 0




