def selectionSort(arr):
    
    for i in range(len(arr)):
        min_x = i

        for item in range(i+1, len(arr)):
            if arr[item] < arr[min_x]:
                min_x = item

        arr[i], arr[min_x] = arr[min_x], arr[i]

arr = [20, 12, 10, 15, 2]
selectionSort(arr)

print(arr)