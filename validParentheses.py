class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)

            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False

            else:
                return False

        return not stack

solution = Solution()
print(solution.isValid("()")) #true
print(solution.isValid("()[]{}")) #true
print(solution.isValid("(]")) #false
print(solution.isValid("([])")) #true