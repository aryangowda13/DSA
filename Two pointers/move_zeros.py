# Move all zeros in an array to the end while maintaining the relative order of the non-zero elements.
def moveZeroes(nums):
    position = 0
# Iterate through the array and move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0: 
            nums[position] = nums[i]
            position += 1
# Fill the remaining positions in the array with zeros
    while position < len(nums):
        nums[position] = 0
        position += 1


nums = [0, 1, 0, 3, 12]

moveZeroes(nums)

print(nums)