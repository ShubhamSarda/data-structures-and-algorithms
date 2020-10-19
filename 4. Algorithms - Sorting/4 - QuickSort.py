def quickSort(my_array):
    qshelper(my_array, 0, len(my_array) - 1)
    return my_array

def qshelper(my_array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while right >= left:
        
        if my_array[left] > my_array[pivot] and my_array[right] < my_array[pivot]:
            my_array[left], my_array[right] = my_array[right], my_array[left]
        
        if my_array[left] <= my_array[pivot]:
            left += 1
        
        if my_array[right] >= my_array[pivot]:
            right -= 1

    my_array[pivot], my_array[right] = my_array[right], my_array[pivot]

    qshelper(my_array, start, right - 1)
    qshelper(my_array, right + 1, end)