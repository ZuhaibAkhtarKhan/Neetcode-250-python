class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = ["(", "[", "{"]
        stack = []

        for p in s:

            if p in b and stack:
                stack.append(p)
            else:
                if (p == ')' and stack[-1] == '(') or (p == ']' and stack[-1] == '[') or (p == '}' and stack[-1] == '{') :
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0


