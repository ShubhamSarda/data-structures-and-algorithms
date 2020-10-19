students = ['andrew', 'akshat', 'chris', 'harshit', 'lary', 'tim', 'drake', 'ashish', 'shubham']

def rondomFunction(students):
    first = students[0] #O(1)
    total = 0 #O(1) 
    new_list = [] #O(1)

    for student in students:
        total += 1 #O(n)
        new_list.append(student) #O(n)
    
    print(new_list) #O(1)   
    return total #O(1)

print(rondomFunction(students)) # O(n) => O(n)