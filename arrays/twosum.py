def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    
nums = [1,2,3,4,5,6]
target = 4
# nums = list(map(int,input("put in the array ").split()))
# target = int(input("Enter the target "))

print(twoSum(nums,target))