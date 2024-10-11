class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n-1


        while left < right:
            current_sm = numbers[left] + numbers[right]
            if current_sm == target:
                return [left + 1, right + 1]
            elif current_sm < target:
                left += 1
            else:
                right -= 1

#just used two pointers algorithm for sorted listy


solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) #[1, 2]
print(solution.twoSum([2,3,4], 6)) #[1, 3]
print(solution.twoSum([-1,0], -1)) #[1, 2]