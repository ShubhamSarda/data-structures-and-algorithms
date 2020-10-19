num_list = [1, 2, 3, 4, 5, 6, 7]
num_list2 = [5, 6, 7, 8, 9]

def rondomFunction(num_list):
    total = 0

    for num1 in num_list2:
        for num2 in num_list:
            print(num1, num2)
            total += 1
    
    return total

print(rondomFunction(num_list))