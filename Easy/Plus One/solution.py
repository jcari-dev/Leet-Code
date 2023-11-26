from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(str(digit) for digit in digits))
        integer += 1
        return [int(digit) for digit in str(integer)]
