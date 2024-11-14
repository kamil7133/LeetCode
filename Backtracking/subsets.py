class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result, sol = [], []

        def backtrack(i):
            if i ==n:
                result.append(sol[:])
                return
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()


        backtrack(0)
        return result

solution = Solution()
print(solution.subsets([1,2,3]))