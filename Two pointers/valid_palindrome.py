# This function checks if a given string is a palindrome.
class Solution:
    # Function to check if a string is a palindrome
    def isPalindrome(self, s: str) -> bool:
        left = 0
        # Initialize the right pointer to the last index of the string
        right = len(s) - 1

        while left < right:
            # Move the left pointer to the right until it points to an alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer to the left until it points to an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare the characters at the left and right pointers (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Take input
s = "A man, a plan, a canal: Panama"

# Call the function
solution = Solution()
answer = solution.isPalindrome(s)

# Print result
print(answer)