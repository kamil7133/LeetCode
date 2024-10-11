from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            output[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums) -1 ,-1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
#test
solution = Solution()
print(solution.productExceptSelf([1,2,3,4])) #expected result [24, 12, 8, 6]
print(solution.productExceptSelf([-1,1,0,-3,3])) #expected result [0,0,9,0,0]


