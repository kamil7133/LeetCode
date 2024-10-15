class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1

solution = Solution()
print(solution.search([-1,0,3,5,9,12], 9))
print(solution.search([-1,0,3,5,9,12], 2))
