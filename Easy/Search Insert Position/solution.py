from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        lower_end = nums[0]

        if lower_end > target:
            return 0

        if nums[-1] < target:
            return len(nums)

        try:
            target_index = nums.index(target)
        except:
            for number in nums:

                if number > lower_end and target > number:
                    lower_end = number

            return nums.index(lower_end)+1

        else:
            return target_index
