import random

numbers = [random.randint(0,100) for x in range(100)]

numbers.sort()

print(numbers)

def binary_search(numbers, target):
    start_index = 0
    end_index = len(numbers) - 1



    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2  # floor division

        if target < numbers[mid_index]:
            end_index = mid_index - 1
        elif target > numbers[mid_index]:
            start_index = mid_index + 1
        else:
                print(f'{target} found at index {mid_index}')
                return numbers[mid_index]
    else:
        print(f'{target} not found!')

binary_search(numbers, 5)
