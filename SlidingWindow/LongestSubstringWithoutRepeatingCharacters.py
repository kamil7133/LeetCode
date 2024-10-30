class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        l = 0
        leng = 0

        for r in range(len(s)):
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[r])
            b = (r - l) + 1
            leng = max(leng, b)
        return leng



#test
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))