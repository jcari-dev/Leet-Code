from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            if number not in seen:
                difference = target - number
                seen[difference] = index
            else:
                return [seen[number], index]
