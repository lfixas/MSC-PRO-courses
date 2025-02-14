### Lists creation and browsing ###
## Create a list that contains 5 numbers and print the first one. ##
def lists_task01():
    list = [0,1,2,3,4,5]
    print(list[0])

## Display the last element of your list. ##
def lists_task02():
    list = [0,1,2,3,4,5]
    print(list[-1])

## Add a 6th element in your list ##
def lists_task03():
    list = [0,1,2,3,4,5]
    list.append(6)
    print(list)

## Display all the elements of your list ##
def lists_task04():
    list = [0,1,2,3,4,5]
    print("All the elements of your list :", end = " ")
    for element in list:
        print(element, end = " ")
    print("")

## Delete the last element and display all the remaining elements ##
def lists_task05():
    list = [0,1,2,3,4,5]
    list.pop()
    print(list)
## Add an element at the beginning of the list and display all its elements. ##
def lists_task06():
    list = [0,1,2,3,4,5]
    list.insert(0,6)
    print(list)

## Display the substring from the 2nd to the 5th elements. ##
def lists_task07():
    list = [0,1,2,3,4,5]
    print(list[2:6])

## Reverse the list by creating a new list with the same elements, ##
##  but starting from the end ##
def lists_task08():
    list = [0,1,2,3,4,5]
    new_list = list[::-1]
    print(new_list)

## Display one element out of two of the list. ##
def lists_task09():
    list = [0,1,2,3,4,5]
    list_one_of_two = list[::2]
    print(list_one_of_two)

## Add 17 elements at the end of your list. ##
def lists_task10():
    list = [0,1,2,3,4,5]
    list.extend([elements for elements in range(17)])
    print(list)

## What does the following code make? ##
def lists_task11_1():
    '''The first code merge the lists named "my_first_list" and "my_second_list" into the list "my_first_list"'''
    my_first_list = [4,5,6]
    my_second_list = [1,2,3]
    my_first_list.extend(my_second_list)
    print(my_first_list)

## Same with: ##
def lists_task11_2():
    '''The second code merge the lists named "my_first_list" and "my_second_list" into the list "my_first_list" but using the elements of the lists directly with the * symbol at the beginning'''
    my_first_list = [7,8,9]
    my_second_list = [4,5,6]
    my_first_list = [*my_first_list,*my_second_list]
    print(my_first_list)
#####

### Operations on lists ###
## Create a list of 10 numbers. ##
## Print the result of the multiplication of all elements of this list. ##
def lists_operations_task01():
    list = [number for number in range (1,11)]
    multi = 1
    for element in list:
        multi *= element 
    print(f"\033[0;36mThe multiplication of all elements of this list is : \033[44m{multi}\033[0m")

## Test this code and try to explain it: ##
def lists_operations_task02():
    '''This code add 10 to x which is taken in the list [3,2,6,7,1,4] and create a list with the results'''
    print([x + 10 for x in [3, 2, 6, 7, 1, 4]])

## Test this code and try to explain it: ##
def lists_operations_task03():
    '''map () applies a given function (in this case, the lambda function) to each item in an iterable (here the list)
    lambda x: is an lambda function that takes the argument "x" and return the square of "x" by "x * x of each item in the iterable.
    In a nutshell, the code create a list with the square of each elements in the list [3, 2, 6, 7, 1, 4]"'''
    print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))

## Browse the list and display both the smallest ##
## and the biggest elements. ##
def lists_operations_task04():
    elements = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
    print(f"\033[0;36mBiggest element of the list : \033[44m{max(elements)}\033[0;36m.\nSmallest element of the list \033[44m{min(elements)}\033[0;36m.\033[0m")

## Display all the elements smaller than 7. ##
def lists_operations_task05():
    elements = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
    print(f"\033[0;36mAll elements small than 7 : \033[44m{sorted(list(filter(lambda x: x < 7, elements)))}\033[0;36m.\033[0m")

## Sort your list in descending order. ##
def lists_operations_task06():
    elements = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
    print(f"\033[0;36mAll elements sort in descending order : \033[44m{sorted(elements,reverse=True)}\033[0;36m.\033[0m")

## Test this code and try to explain it: ##
def lists_operations_task07():
    '''This code take x in a list ([42,3,4,18,3,10]).
    For each x, if x is even, it take the half of x
    if the the results in a list'''
    print([x//2 if x%2 == 0 else x*2 for x in [42,3,4,18,3,10]])

## Test this code and try to explain it: ##
def lists_operations_task08():
    '''This code take x in a list ([42,3,4,18,3,10]).
    For each x, if it's bigger than 10, it put remind the list.
    In the other case, it is being remove.'''
    print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))

## Test this code and try to explain it: ##
def lists_operations_task09():
    '''This code return an enumerator object.
    It generates pairs of index-value pairs, starting from 0.
    It return these pairs in a list.'''
    print([*enumerate([42, 3, 4, 18, 3, 10])])

## Test this code and try to explain it: ##
def lists_operations_task10():
    '''This code combines two lists of first names and last names, manipulates them using slicing.
    zip is used to combine elements from first_name and last_name in reversed order.
    Then, print deferent index of the list.'''
    first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
    last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
    magic = [* zip ( first_name , last_name [:: -1]) ]
    print ( magic [0])
    print ( magic [3])
    print ( magic [1][0])
    print ( magic [0][1])
    print ( magic [2])
#####

### Dictionaries ###
## Create a dictionary stored in a student variable. ##
## This dictionary must contain 2 key/value pairs. ##
## The keys must be “name” and “academic_year”. ##
## The associated values are up to you, but please keep them coherent! ##
def dictionaries_task01():
    student =	{"name": "Lucas", "academic_year": "2023-2026"}
    print(student)

## In your student dictionary, add a units key. ##
## The value associated to units is an array of 3 elements. ##
## Each element of this array is a dictionary of 3 keys: ##
## name, credits, grade: ##
def dictionaries_task02():
    student =	{"name": "Lucas", "academic_year": "2023-2026", "unit": {"name": "Web Development", "credits": "120", "grade": "A"}}
    print(student)
## Create a new directory named grade_weight_mapping. ##
## This dictionary contains 5 keys (“A”, “B”, “C”, “D”, “E”) ##
## and their respective values (4, 3, 2, 1, 0). ##
def dictionaries_task03():
    grade_weight_mapping = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}
    student =	{"name": "Lucas", "academic_year": "2023-2026", "unit": {"name": "Web Development", "credits": "120", "grade": "A"}, "total_credits": ""}
    total_credits = student["unit"]["credits"]
    grade = student["unit"]["grade"]
    gpa = grade_weight_mapping.get(grade)
    student["total_credits"] = total_credits
    student["GPA"] = gpa
    print(student)

## Create an array and store at least 3 students 
## (as defined in previous tasks) in it. ##
## Write some code to: ##
def dictionaries_task04():
    grade_weight_mapping = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}
    student_01 = {
    "name": "Lucas",
    "academic_year": "2023-2026",
    "unit": {
        "name": "Web Development",
        "credits": 120,
        "grade": "A"
    },
    "total_credits": "",
    "GPA": ""
}
    student_02 = {
    "name": "Emma",
    "academic_year": "2023-2026",
    "unit": {
        "name": "Data Science",
        "credits": 90,
        "grade": "B"
    },
    "total_credits": "",
    "GPA": ""
}
    student_03 = {
    "name": "Sophia",
    "academic_year": "2023-2026",
    "unit": {
        "name": "Computer Science",
        "credits": 110,
        "grade": "A"
    },
    "total_credits": "",
    "GPA": ""
}
    student_04 = {
    "name": "Liam",
    "academic_year": "2023-2026",
    "unit": {
        "name": "Mathematics",
        "credits": 100,
        "grade": "B"
    },
    "total_credits": "",
    "GPA": ""
}
    student_05 = {
    "name": "Olivia",
    "academic_year": "2023-2026",
    "unit": {
        "name": "Art History",
        "credits": 80,
        "grade": "C"
    },
    "total_credits": "",
    "GPA": ""
}
    students = []
    students.extend([student_01, student_02, student_03, student_04, student_05])
    for student in students:
        total_credits = student["unit"]["credits"]
        grade = student["unit"]["grade"]
        gpa = grade_weight_mapping.get(grade)
        student["total_credits"] = total_credits
        student["GPA"] = gpa
    sorted_by = str(input("\033[1;32mHow do you want to sort your students list? (name/GPA): \033[0m")).upper()
    sorted_abc = str(input("\033[1;32mHow do you want to sort your students list? (asc/des): \033[0m")).upper()
    if sorted_by == "NAME" and sorted_abc == "ASC":
        students_sorted = sorted(students, key=lambda x: x["name"],reverse = True)
        print("\033[1;33mSorted by name ascending\033[0m")
    elif sorted_by == "NAME": 
        students_sorted = sorted(students, key=lambda x: x["name"])
        print("\033[1;33mSorted by name descending\033[0m")
    if sorted_by == "GPA" and sorted_abc == "ASC":
        students_sorted = sorted(students, key=lambda x: x["GPA"])
        print("\033[1;33mSorted by GPA ascending\033[0m")
    elif sorted_by == "GPA":
        students_sorted = sorted(students, key=lambda x: x["GPA"],reverse = True)  
        print("\033[1;33mSorted by GPA descending\033[0m")
    students = students_sorted
    print(f"\033[0;36m{students}\033[0m")
######

### Lets’ go further ###
## Let’s consider a list of names (the ambassador’s banquet guests). ##
## Write a program that displays: ##
## ✓ “welcome in” if a given name belongs to this list ; ##
## ✓ and “get lost!” otherwise. ##
def further_task01():
    guests = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Ella",
    "Frank",
    "Grace",
    "Hannah",
    "Isaac",
    "Julia",
    "Katherine",
    "Liam",
    "Mia",
    "Noah",
    "Olivia",
    "Penelope",
    "Quinn",
    "Riley",
    "Sophia",
    "Thomas",
    "Ursula",
    "Victoria",
    "William",
    "Xander",
    "Yasmine",
    "Zachary",
    "Amelia",
    "Benjamin",
    "Chloe",
    "Daniel",
    "Emily",
    "Fiona",
    "George",
    "Hazel",
    "Isabella",
    "Jacob",
    "Kayla",
    "Lucas",
    "Mila",
    "Nathan",
    "Oliver",
    "Piper",
    "Quincy",
    "Rebecca",
    "Samuel",
    "Taylor",
    "Ulysses",
    "Violet",
    "Wyatt",
]
    name  = str(input("\033[0;32mWhat's your name? : \033[0m")).capitalize()
    if name in guests:
        print("\033[1;32mWelcome in\033[0m")
    else :
        print("\033[1;31mGet lost!\033[0m")

## Write a program that deletes all the duplicated elements in a list. ##
def further_task02():
    names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Ella",
    "Frank",
    "Grace",
    "Hannah",
    "Isaac",
    "Julia",
    "Katherine",
    "Liam",
    "Mia",
    "Noah",
    "Olivia",
    "Penelope",
    "Quinn",
    "Riley",
    "Sophia",
    "Thomas",
    "Ursula",
    "Victoria",
    "William",
    "Xander",
    "Yasmine",
    "Zachary",
    "Amelia",
    "Benjamin",
    "Chloe",
    "Daniel",
    "Emily",
    "Fiona",
    "George",
    "Hazel",
    "Isabella",
    "Jacob",
    "Kayla",
    "Lucas",
    "Mila",
    "Nathan",
    "Oliver",
    "Piper",
    "Quincy",
    "Rebecca",
    "Samuel",
    "Taylor",
    "Ulysses",
    "Violet",
    "Wyatt",
    "Alice",  # Duplicate
    "David",  # Duplicate
    "Hazel",  # Duplicate
    "Liam",   # Duplicate
    "Mia",    # Duplicate
    "Oliver", # Duplicate
    "Emily",  # Duplicate
    "Jacob",  # Duplicate
    "Noah",   # Duplicate
    "Sophia", # Duplicate
]
    new_names = []
    for name in names:
        if name not in new_names:
            new_names.append(name)
    print(f"\033[0;36mLength before : {len(names)}\nLength after : {len(new_names)}\033[0m")
## Write a program that, given a name, displays all the meetings ##
## in which this person is involved. ##
def further_task03():
    meetings = [
    ["Monday", "3:30 PM", "Joe", "Samantha"],
    ["Tuesday", "10:00 AM", "Alice", "Bob"],
    ["Wednesday", "2:45 PM", "Lucas", "Mia"],
    ["Thursday", "11:30 AM", "Ella", "Frank"],
    ["Friday", "4:15 PM", "Mia", "Joe"],
    ["Monday", "1:00 PM", "Isaac", "Julia"],
    ["Tuesday", "9:30 AM", "Katherine", "Lucas"],
    ["Wednesday", "3:00 PM", "Mia", "Noah"],
    ["Thursday", "2:15 PM", "Joe", "Penelope", "Lucas"],
    ["Friday", "5:45 PM", "Lucas", "Ella"]
]
    name  = str(input("\033[0;32mName of a person : \033[0m")).capitalize()
    involved = []
    for meeting in range(len(meetings)):
        if name in meetings[meeting]:
            involved.append(meetings[meeting])
    if len(involved) == 0:
        involved = "\033[0;33mThis person is not involved in any meetings\033[0m"
    print(f"\033[0;34m{involved}\033[0m")
#####
further_task03()
### Challenge ###
## Create a list of 1 000 000 random integers ##
## and sort it as fast as possible. ##
import time
import random
def Challenge():
    startingTime = time.time()
    list = [random.randrange(1000000) for i in range(0,1000000)]
    list.sort()
    duration = time.time()-startingTime
    print(duration)
#####