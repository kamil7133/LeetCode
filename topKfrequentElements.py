class Solution(object):
    def topKFrequent(self, nums, k):
        seen = {} #making empty hashmap
        for num in nums: #iterate every number in input list
            if num not in seen: #if number isn't in hashmap make it =1
                seen[num] = 1
            else:
                seen[num] += 1 #if it is in, +1
        sorted_seen = sorted(seen.items(), key=lambda x: x[1], reverse=True) #sorting hashmap
        top_k_items = sorted_seen[:k] #slicing hashmap to k elements
        top_k_elements = [item[0] for item in top_k_items] #pulling values
        return top_k_elements



#test
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3],2)) #expected result [1,2]
print(solution.topKFrequent([1],1)) #expected result [1]
