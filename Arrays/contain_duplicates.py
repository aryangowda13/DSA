# Check if the array contains any duplicate elements
def containsDuplicate(nums):
#   Create a set to store the unique elements
    seen = set()

    for num in nums:
        # Check if the current number is already in the set
        if num in seen:
            return True
        # If not, add the number to the set
        seen.add(num)

    return False

# Taking input
nums =  list(map(int, input("Enter numbers separated by spaces: ").split()))  # Example input with duplicates

# Calling the function
result = containsDuplicate(nums)
print("Contains duplicate:", result)