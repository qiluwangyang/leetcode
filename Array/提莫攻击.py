from typing import List


class Solution:
    @staticmethod
    def findPoisonedDuration(time_series: List[int], duration: int) -> int:
        count_duration = 0
        if not time_series:
            return count_duration
        for index in range(1, len(time_series)):
            if time_series[index] - time_series[index - 1] < duration:
                count_duration += time_series[index] - time_series[index - 1]
            else:
                count_duration += duration
        return count_duration + duration


solution = Solution()
print(solution.findPoisonedDuration([1, 4], 2))
