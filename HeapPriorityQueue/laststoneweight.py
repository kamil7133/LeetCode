import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            l = heapq.heappop(stones)
            next_l = heapq.heappop(stones)

            if l != next_l:
                heapq.heappush(stones, l - next_l)

        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0


solution = Solution()
print(solution.lastStoneWeight([2,7,4,1,8,1]))