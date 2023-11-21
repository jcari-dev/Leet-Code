class Solution:

    # This solution is a tiny bit more complex and overworked
    # than usual by the simple fact that we are not converting
    # into a string to know if it is a palindrome.

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_int = 0

        original_int = x

        while x > 0:
            x_last_digit = x % 10

            reversed_int = reversed_int * 10 + x_last_digit

            x //= 10

        return original_int == reversed_int
