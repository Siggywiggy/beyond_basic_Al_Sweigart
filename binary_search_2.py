import random

nums = [random.randint(0,25) for num in range(20)]
nums.sort()

print(nums)

# binary search algo ONLY works on pre-sorted arrays!

def binary_search(nums,target):
    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if nums[middle_index] == target:
            print(f'{target} found at index {middle_index}')
            return middle_index
        elif target < nums[middle_index]:
            end_index = middle_index - 1
        elif target > nums[middle_index]:
            start_index = middle_index + 1

        #else: # else the target == nums[mid_index]
           # print(f'{target} found at index {middle_index}')
            #return middle_index
    else:
        print(f'{target} not found!')

print(binary_search(nums, 9))