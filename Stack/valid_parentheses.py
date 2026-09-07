class Solution:
    # Check if the input string has valid parentheses
    def isValid(self, s):
        stack = []
    # Define the mapping of closing to opening brackets
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:
         # If the bracket is an opening bracket, push it onto the stack
            if bracket in "([{":
                stack.append(bracket)

            else:
                if not stack or stack[-1] != pairs[bracket]:
                    return False

                stack.pop()

        return len(stack) == 0


# Input is already given here
s = "([])"

obj = Solution()
answer = obj.isValid(s)

print("Input:", s)
print("Answer:", answer)