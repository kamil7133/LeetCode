class Solution(object):
    def twoSum(self, nums, target):
        seen = {} #empty hashmap

        for i, num in enumerate(nums): #iterate every index and number in input nums //i -> index //num -> value
            comp = target - num #count what number we need to make target

            if comp in seen: #checking if number is already in hashmap
                return [seen[comp], i]

            seen[num] = i

#test
solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) # expected result: [0,1]
print(solution.twoSum([3,2,4], 6)) #expected result: [1,2]
print(solution.twoSum([3,3], 6)) #expected result: [0,1]