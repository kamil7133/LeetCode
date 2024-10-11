class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        final_result = []
        self.DFS(n, "", 0, 0, final_result)
        return final_result

    def DFS(self, n, current_combination, open, close, final_result):
        if open == n and close == n:
            final_result.append(current_combination)
            return

        if open < n:
            self.DFS(n, current_combination + "(", open + 1, close, final_result)

        if close < open:
            self.DFS(n, current_combination + ")", open, close + 1, final_result)

solution = Solution()
print(solution.generateParenthesis(3))











#inspired by this DFS algorithm https://github.com/msambol/dsa/blob/master/search/depth_first_search.py