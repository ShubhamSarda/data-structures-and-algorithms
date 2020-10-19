
def binarySearch(my_array, target):
    left = 0
    right = len(my_array) - 1
    result = helper(my_array, target, left, right)
    return result

def helper(my_array, target, left, right):
    if left > right:
        return -1
    
    middle = (left + right) // 2
    middle_element = my_array[middle]

    if target == middle_element:
        return middle
    elif target < middle_element:
        right = middle - 1
        result = helper(my_array, target, left, right)
        return result
    else:
        left = middle + 1
        result = helper(my_array, target, left, right)
        return result