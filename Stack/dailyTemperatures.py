class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        container = []

        for i in reversed(range(len(temperatures))):
            while container and temperatures[i] >= temperatures[container[-1]]:
                container.pop()

            if container:
                result[i] = container[-1] - i

            container.append(i)

        return result





#test
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
