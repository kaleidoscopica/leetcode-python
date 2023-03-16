### 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return bool
        is_palindrome = True

        # stack variable
        stack = []

        # integer as a string
        string_x = str(x)

        # number of digits in integer
        x_len = len(string_x)

        # Iterate through each digit in the integer
        for idx, digit in enumerate(string_x):
            # If we're less than halfway through the digits, add this one to the stack
            if idx < x_len//2:
                stack.append(digit)
            # Next, see if we're dealing with an even number of digits
            if x_len % 2 == 0:
                # Then we're at or over halfway through the digits,
                # pop one from the stack and compare it. If it's not the same,
                # set is_palindrome equal to False
                if idx >= x_len//2:
                    popped = stack.pop()
                    if popped != digit:
                        is_palindrome = False
            # Else, we must be dealing with an odd number of digits
            else:
                # Same thing here. If we're over halfway through the digits,
                # pop one from the stack and compare it. If it's not the same,
                # set is_palindrome equal to False
                if idx > x_len//2:
                    popped = stack.pop()
                    if popped != digit:
                        is_palindrome = False

        return is_palindrome
