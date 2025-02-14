### Conditionals ###
## Evaluate and explain the following lines: ##
def conditionals_task00():
    '''(42 > 12) # check if 42 is superior than 12, return True
    (12 = 12) # try to put a number in a variable named 12, doesn't work
    (12 == 12) # check if 12 equals 12, return True
    (“hello” == “world”) # check if "hello" is "world", return False
    (218 >= 118) # check if 218 equals of superior of 118, return True
    (“a”.upper() == “A”) # check if the upper of "a" if "A", return True
    (1 ∗ 2 ∗ 3 ∗ 4 <= 9) # check if 1*2*3*4 equals of inferior of 9, return False
    (“z” in “azerty”) # check if "z" is in "azerty", return True
    '''
## Ask an integer to the user: ##
def conditionals_task01():
    integer = int(input("\033[0;34mWhat is your favorite integer? : \033[0m"))
    if integer == 42:
        print("\033[1;32mCorrect answer\033[0m")
    else :
        print("\033[1;31mNo interest...\033[0m")

## Ask an integer to the user: ##
## ✓ if it’s odd, display “This integer is odd” ; ##
## ✓ if it’s even, display “This integer is even”. ##
def conditionals_task02():
    integer = int(input("\033[0;34mGive me an integer : \033[0m"))
    if integer%2 == 1:
        print("\033[0;36mThis integer is \033[1;36modd\033[0m")
    else:
        print("\033[0;36mThis integer is \033[1;36meven\033[0m")

## Ask the user to input a string: ##
## ✓ if it’s “open sesame”, display “access granted” ; ##
## ✓ if it’s "will you open, you goddamn !¤*@¡‘, display ##
## ”access fucking granted" ; ##
## ✓ else, display “permission denied”. ##

def conditionals_task03():
    string = str(input("\033[0;34mPassword : \033[0m"))
    if string == "open sesame":
        print("\033[1;32mAcces granted\033[0m")
    elif string == "will you open, you goddamn !¤*@¡":
        print("\033[42mAccess fucking granted\033[0m")
    else:
        print("\033[4;31mPermission denied\033[0m")

## Ask the user to input an integer: ##
## ✓ if it’s 42, display “OK” ; ##
## ✓ if it’s smaller or equal than 21, display “OK” ; ##
## ✓ if it’s even, display “OK” ; ##
## ✓ if this integer divided by 2 is smaller than 21 (excluded), ##
## display “OK” ; ##
## ✓ finally, if it’s is odd and greater or equal than 45, ##
## display “OK” ; ##
## ✓ in any other cases, display “You got wrong my poor friend!”. ##
def conditionals_task04():
    integer = int(input("\033[0;34mGive me an integer : \033[0m"))
    if integer == 42 or integer <= 21 or integer%2 == 0 or integer/2 < 21 or (integer%2 == 1 and integer >= 45):
        print("\033[1;32mOK\033[0m")
    else :
        print("\033[41mYou got wrong my poor friend!\033[0m")        

## Execute and fix the following code: ##
def conditionals_task05():
    a = 42
    b = 41
    if a == b:
        print ("A and B are equal")
    if b <= a:
        print ("B is less than of equal to A")
    if b != a:
        print ("B is different from A")
#####

### Loops ###
## Display all integers from 1 to 1000. ##
def loops_task00():
    for integers in range (1,1001):
        print(integers, end= "|")

## Ask the user a string. ##
## Display all the characters of this string twice. ##
## For instance: “taxi” will become “ttaaxxii”. ##
def loops_task01():
    string = str(input("\033[0;34mI ask you for a string : \033[0m"))
    string_twice = []
    string_tab = [*string]
    for character in string_tab:
        string_twice.append(character*2)
    string_new = "".join(string_twice)
    print(f"\033[0;36m{string_new}\033[0m")

## Print all integers divisible by 7 from 10 000 to 1. ##
def loops_task02():
    for integer in reversed(range(1,10001)):
        print(f"| {integer}/7 = {round(integer/7,2)} |")

## For all integers from -30 to 30: ##
## ✓ if it’s a multiple of 3, display “Fizz” ##
## ✓ if it’s a multiple of 5, display “Buzz” ##
## ✓ if it’s a multiple of 3 and 5, display “FizzBuzz” ##
## ✓ if it does not meet any of the previous conditions, ##
## just print the integer itself. ##
def loops_task03():
    for integer in range(-30,31):
        if integer%3 == 0 and integer%5 == 0:
            print(f"\033[0;33m{integer} \033[0;36mFizz\033[0;35mBuzz\033[0m")
        elif integer%3 == 0:
            print(f"\033[0;33m{integer} \033[0;36mFizz\033[0m")
        elif integer%5 == 0:
            print(f"\033[0;33m{integer} \033[0;35mBuzz\033[0m")
        else:
            print(f"\033[1;33m{integer}\033[0m")

## Generate the lyrics of the song ##
## “99 bottles of age appropriate bottles on the wall”. ##
## The songs ends when there is no more bottles on the wall ##
def loops_task04():
    print("\033[0;34m==========================================\033[0m")
    print("\033[1;32m\"99 Bottles of Age-Appropriate Beverage\"\033[0m")
    print("\033[0;32m from \033[3;32mThe Amazing World of Gumball\033[0m")
    print("\033[0;34m==========================================\033[0m")
    for bottles in reversed(range(1,100)):
        if bottles == 1:
            print("🎶 One bottle of age-appropriate beverage on the wall 🎵\n"*2)
        else :
            print(f"🎶 {bottles} bottles of age-appropriate beverage on the wall 🎵\n"*2)
        print("          🎶 \033[3;37mTake one down, pass it around\033[0m 🎵\n")
    print("🎶 \033[3;37mna! na!na!~ na!~ na!-na!na!na!na!~ na!na!na!na~ na! na! na!~~\033[0m 🎵\n"*3)

## Write a program that takes an n integer as input and displays, ##
## for each integer from 2 to n/2, the list of its multiples ##
## strictly smaller than n, in descending order. ##
def loops_task05(integer):
    for multiplice in range(2, int(integer/2)+1):
        for n in reversed(range(multiplice, integer, multiplice)):
            print(n, end = " ")
        print("")
#####

### Encryption ###
## Print the result of the encryption of Caesar Cipher. ##
def encryption_task01():
    message = str(input("\033[0;34mYour message to be encrypted : \033[0m"))
    key = int(input("\033[0;34mThe key on encryption : \033[0m"))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_encrypted = ""
    message = message.upper()
    for message_letter in [*message]:
        if message_letter == " ":
            message_encrypted += " "
        for alphabet_number in range(len([*alphabet])):
            if message_letter.find([*alphabet][alphabet_number]) > -1:
                if alphabet_number+key > 26:
                    message_encrypted += [*alphabet][alphabet_number+key-26*((alphabet_number+key)//26)]
                else :
                    message_encrypted += [*alphabet][alphabet_number+key]
    print(f"\033[0;36mEncrypted message : \033[44m{message_encrypted}\033[0m")
    return message_encrypted

def encryption_task01_5():
    message = encryption_task01()
    key = int(input("\033[0;34mThe key on encryption : \033[0m"))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_decrypted = ""
    for message_letter in [*message]:
        if message_letter == " ":
            message_decrypted += " "
        for alphabet_number in range(len([*alphabet])):
            if message_letter.find([*alphabet][alphabet_number]) > -1:
                if alphabet_number+key > 26:
                    message_decrypted += [*alphabet][alphabet_number-key-26*((alphabet_number-key)//26)]
                else :
                    message_decrypted += [*alphabet][alphabet_number-key]
    print(f"\033[0;36mEncrypted message : \033[44m{message_decrypted}\033[0m")
## Write a program that can encrypt or decrypt a text using a ##
##  Vigenere code ##
def encryption_task02():
    message = str(input("\033[0;34mYour message to be encrypted : \033[0m"))
    key_message = str(input("\033[0;34mThe key on encryption : \033[0m"))
    encrypt = str(input("\033[0;34mEncrypt(Yes) or decrypt (No)? : \033[0m"))
    if encrypt == "Yes":
        encrypt = True
    elif encrypt == "No":
        encrypt = False
    else :
        print("\033[0;31mPlease, retry\033[0m")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_encrypted = ""
    message = message.upper()
    key_message = key_message.upper()
    key_len = len(key_message)
    key_pos = 0
    for message_letter in [*message]:
        if message_letter == " ":
            message_encrypted += " "
            key_pos -= 1
        if key_pos >= key_len:
            key_pos = 0
        if encrypt:
            for alphabet_number in range(len([*alphabet])):
                if message_letter.find([*alphabet][alphabet_number]) > -1:
                    if alphabet_number+(ord(key_message[key_pos])-65) > 26:
                        message_encrypted += [*alphabet][(alphabet_number+ord(key_message[key_pos])-65)-26*((alphabet_number+ord(key_message[key_pos])-65)//26)]
                    else :
                        message_encrypted += [*alphabet][alphabet_number+(ord(key_message[key_pos])-65)]
        else :
            for alphabet_number in range(len([*alphabet])):
                if message_letter.find([*alphabet][alphabet_number]) > -1:
                    if alphabet_number+(ord(key_message[key_pos])-65) > 26:
                        message_encrypted += [*alphabet][(alphabet_number-ord(key_message[key_pos])-65)-26*((alphabet_number-ord(key_message[key_pos])-65)//26)]
                    else :
                        message_encrypted += [*alphabet][alphabet_number-(ord(key_message[key_pos])-65)]
        key_pos += 1
    print(f"\033[0;36mEncrypted message : \033[44m{message_encrypted}\033[0m")

#####
encryption_task02()
### Challenge ###
## Write the shortest possible code that realizes the following: ##
## ✓ ask the user for an integer and a string ; ##
## ✓ if this integer is 0, then quit ; ##
## ✓ if the string contains a vowel, display the integer ; ##
## ✓ if the integer is greater or equal than 42, display the integer ; ##
## ✓ else display the string. ##
def Challenge():
    integer = int(input("\033[0;34mI ask you for an integer : \033[0m"))
    string = str(input("\033[0;34mI ask you for a string : \033[0m"))
    vowels = ["A","a","E","e","I","i","O","o","U","u","Y","y"]
    if integer == 0:
        return
    for check_vowels in vowels:
        if string.find(check_vowels) > -1:
            print(integer)
            return
    if integer >= 42:
        print(integer)
        return
    print(string)  
#####
