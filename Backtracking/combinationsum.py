class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        r, s = [], []
        n = len(candidates)

        def backtrack(i, c_s):
            if c_s == target:
                r.append(s[:])
                return

            if c_s > target or i == n:
                return

            backtrack(i+1, c_s)

            s.append(candidates[i])

            backtrack(i, c_s+candidates[i])

            s.pop()

        backtrack(0, 0)
        return r




solution = Solution()
print(solution.combinationSum([2,3,6,7], [7]))