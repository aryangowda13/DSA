def generateParenthesis(n):
    result = []
# defining a backtrack function to generate valid parentheses combinations
    def backtrack(current, open_count, close_count):

        # If we have used all parentheses
        if len(current) == 2 * n:
            result.append(current)
            return

        # We can add '(' if we still have some left
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        # We can add ')' only when there is an unmatched '('
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)

    return result


# Already given input
n = 3

print(generateParenthesis(n))