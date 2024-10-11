class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sm = a + nums[left] + nums[right]
                if current_sm == 0:
                    result.append([a, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sm < 0:
                    left += 1
                else:
                    right -= 1
        return result







#test
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4])) #[[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([0,1,1])) #[]
print(solution.threeSum([0,0,0])) #[[0, 0, 0]]