class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() #changing all big letters
        s = ''.join(filter(str.isalnum, s)) #deleting all non number non letter characters

        return s == s[::-1]
#test
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama")) #expected True
print(solution.isPalindrome("race a car")) # expected False
print(solution.isPalindrome("")) #expected True