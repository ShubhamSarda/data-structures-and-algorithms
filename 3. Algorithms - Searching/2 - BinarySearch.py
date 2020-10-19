def binarySearch(my_array, target):
    left = 0
    right = len(my_array) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = my_array[middle]

        if target == middle_element:
            return middle
        elif target < middle_element:
            right = middle - 1
        else:
            left = middle + 1

    return -1

### Test 1 ###
print(binarySearch([1, 5, 10, 12, 25, 30, 32], 29))

### Test 2 ###
print(binarySearch([5, 10, 15, 20, 25], 15))