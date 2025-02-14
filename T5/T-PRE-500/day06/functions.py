### Basic functions ###
## Can you explain this piece of code? ##
def basic_functions_task00():
    def f(x):
        return 2 * x + 1
    def g():
        return 7
    
    y = f(2) # use the f(x) function with 2 as x that return 2*x+1 meaning that y is now 2*2+1 = 5
    print (y)

    y = f(5) + g() # use the f(x) and g() function with 5 as x that return 2*x+1 = 2*5+1 = 11 and g() that return 7, meaning that y is now 11 + 7 = 18
    print(y)

## Using the following functions, display a lettuce-tomato-double ##
##  ham sandwich in your terminal. ##
def basic_functions_task01():
    def bread():
        print ("\033[0;30m <////////// > \033[0m")
    def lettuce():
        print ("\033[0;32m ~~~~~~~~~~~~ \033[0m")
    def tomato():
        print ("\033[0;31m O O O O O O \033[0m")
    def ham():
        print ("\033[0;35m ============ \033[0m")

    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

## Make 42 of those lettuce-tomato-double ham sandwiches. ##
def basic_functions_task02():
    for sandwiches in range(1,43):
        print(f"\n\033[44mSandwiches n°{sandwiches}\033[0m\n")
        basic_functions_task01()

## Write a function that takes the number of sandwiches ##
## to prepare as a parameter and displays as ##
## many sandwiches as requested. ##
def basic_functions_task03(order):
    if order <= 0 :
        print("\033[41mI can't do this\033[0m")
    else :
        for sandwiches in range(1,order+1):
            print(f"\n\033[44mSandwiches n°{sandwiches}\033[0m\n")
            basic_functions_task01()

## Add a new parameter to your previous function. ##
## It should provide the possibility to make a vegetarian sandwich ##
## (double vegetables and no ham). ##
## If this option is not specified, by default, ##
## the sandwich must be a lettuce-tomato-double ham one. ##
def basic_functions_task04(order,type="default"):
    def bread():
        print ("\033[0;30m <////////// > \033[0m")
    def lettuce():
        print ("\033[0;32m ~~~~~~~~~~~~ \033[0m")
    def tomato():
        print ("\033[0;31m O O O O O O \033[0m")
    def vege():
        bread()
        lettuce()
        lettuce()
        tomato()
        tomato()
        bread()
    if order <= 0 :
        print("\033[41mI can't do this\033[0m")
    else :
        if type == "default":
            for sandwiches in range(1,order+1):
                print(f"\n\033[44mSandwiches n°{sandwiches}\033[0m\n")
                basic_functions_task01()
        elif type == "vege":
            for sandwiches in range(1,order+1):
                print(f"\n\033[44mVegetarian sandwiches n°{sandwiches}\033[0m\n")
                vege()
#####

### Recursion ###
## Write a recursive function that tests if a string is a palindrome, ## ## such as “kayak”, “never odd or even” or “Was it a car or a cat I saw?”. ##
def recursion_task01():
    string = str(input("\033[0;34mIs it a palindrome? : \033[0m"))
    string_changed = string.replace(" ", "").lower()
    punctuation = ["!","?","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","'","{","|","}","~"]
    for replace_punctuation in punctuation:
        string_changed = string_changed.replace(replace_punctuation, "")
    for lenght in range(len(string_changed)//2):
        if string_changed[lenght] != string_changed[-(lenght+1)]:
            print("\033[1;31mIs not a palindrome\033[0m")
            return
    print ("\033[1;32mIs a palindrome\033[0m")

## Write a program that lists all the files and directories ##
## in the current directories, as well as all files ##
## and directories in its sub-directories and so on. ##       
def recursion_task02(path):
    import os
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            print(f"\033[1;34mDirectory:\033[22m {entry_path}\033[0m")
            recursion_task02(entry_path)
        else:
            print(f"\033[1;36mFile:\033[22m {entry_path}\033[0m")
#####

### Higher-order functions ###
## Write 5 functions, each taking a string s and an integer n ##
## as parameters and returning a boolean: ##
## ✓ funA checks if s contains at least n lowercase letters; ##
## ✓ funB checks if s contains at least n uppercase letters; ##
## ✓ funC checks if s contains at least n characters; ##
## ✓ funD checks if s contains at least n special characters; ##
## ✓ funE checks if s contains at least n numbers. ##
def higher_order_task00(s,n):
    import string
    def funA(s,n):
        lowercases = sum(1 for check in s if check.islower())
        # for check in s:
        #     if check.islower() :
        #         lowercases += 1
        return lowercases >= n
        # if lowercases >= n:
        #     return True
        # else :
        #     return False
    def funB(s,n):
        uppercases = sum(1 for check in s if check.isupper())
        return uppercases >= n
    def funC(s,n):
        characters = len(s)
        return characters >= n
    def funD(s,n):
        special = sum(1 for check in s if check in string.punctuation)
        return special >= n
    def funE(s,n):
        digits = sum(1 for check in s if check in string.digits)
        return digits >= n

    print(f"\033[0;46m ⎇ \"{s}\" contains at least {n} lowercase letters is at \033[1m{funA(s,n)}\033[0m")
    print(f"\033[0;46m ⎇ \"{s}\" contains at least {n} uppercase letters is at \033[1m{funB(s,n)}\033[0m")
    print(f"\033[0;46m ⎇ \"{s}\" contains at least {n} characters is at \033[1m{funC(s,n)}\033[0m")
    print(f"\033[0;46m ⎇ \"{s}\" contains at least {n} special characters is at \033[1m{funD(s,n)}\033[0m")
    print(f"\033[0;46m ⎇ \"{s}\" contains at least {n} numbers is at \033[1m{funE(s,n)}\033[0m")

## Write a generic function that checks if a password is valid. ##
def higher_order_task01():
    password = str(input("\033[0;34mPlease enter your password: \033[0m"))
    def check_password(t,n,s):
        import string
        if t == "lower":
            lowercases = sum(1 for check in s if check.islower())
            return lowercases >= n
        elif t == "special":
            special = sum(1 for check in s if check in string.punctuation)
            return special >= n
        else:
            print("\033[1;31mInvalid password type\033[0m")

    is_valid = check_password("lower",4,password) and check_password("special",2,password)
    if is_valid:
        print("\033[0;42mValid password\033[0m")
    else:
        print("\033[0;41mInvalid password\033[0m")

#####
# higher_order_task01()
### Challenge ###
## Write a little program that computes the power function ##
## as fast as possible. ##
## How long does it take to compute 42**84? ##
## How long does it take to compute 42**168? ##
def Challenge(number,power):
    import time
    startingTime = time.time()
    result = 1
    for loop_power in range(power):
        result *= number
    print(f"\033[44m{result}\033[0m")
    duration = time.time()-startingTime
    print(duration)
#####