class Solution:
    def longestConsecutive(self, nums):
        if not nums: #first of all, checking if input have numbers
            return 0

        numset = set(nums) #making empty set
        longest_streak = 0 #making variable for longest streak

        for num in numset: #iterate every number in set
            if num - 1 not in numset: #checking first number of sequence
                current_num = num
                current_streak = 1 #every first number make streak 1

            while current_num + 1 in numset: #iterate every number bigger than first of streak, if there is no more bigger value program stop
                current_num +=1
                current_streak +=1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


#test
solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2,])) #expected result: 4
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #expected result: 9