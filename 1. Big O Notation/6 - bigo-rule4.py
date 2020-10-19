#Rule 4 - Consider different variable for different inputs 

num_list = [1, 2, 3, 4, 5, 6, 7]

def rondomFunction(num_list, char_list):

    for num in num_list:
        print(num) #O(n)

    for num in num_list:
        print(num) #O(n)

print(rondomFunction(num_list, char_list)) #O(n + n) => O(2n) => O(n)