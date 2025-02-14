### Strings ###
## Store a string in a variable. Then, print it ##
def Strings_Task00():
    string = input("\033[1;32mWhat do you want to use ? : \033[0m")
    print("\033[1;33mYour string : \033[0;34m",string, "\033[0m")

## Print the 1st character of your string. ##
## And also the 5th one. ##
def Strings_Task01():
    string = input("\033[1;32mWhat do you want to use ? : \033[0m")
    print("\033[1;33mThe 1st character of your string : \033[0;34m",string[0],"\033[0m")
    print("\033[1;33mThe 5th character of your string : \033[0;34m",string[4],"\033[0m")

## Print the last character of your string. ##
def Strings_Task02():
    string = input("\033[1;32mWhat do you want to use ? : \033[0m")
    print("\033[1;33mThe last character of your string : \033[0;34m",string[-1],"\033[0m")

## In one line, print from the 5th to the 10th character of this string. ##
def Strings_Task03():
    string = input("\033[1;32mWhat do you want to use ? : \033[0m")
    print("\033[1;33mFrom the 5th to the 10th character of your string : \033[0;34m",string[4:10],"\033[0m")
#####

### String methods ###
## Write a snippet of code that transforms any string in lower case. ##
def Strings_methods_Task00():
    string = input("\033[1;32mWhat do you want to use ? : \033[0m")
    print("\033[1;33mYour string in lower case : \033[0;34m",string.lower(),"\033[0m")

## Write a snippet of code that replaces every “tu” in a string by “ta” ##
def Strings_methods_Task01():
    string = input("\033[1;32mWhat do you want to use ? : \033[0m")
    print("\033[1;33mYour string with ""tu"" by ""ta"" : \033[0;34m",
    string.replace("tu", "ta"),"\033[0m")

## Explain the following code and its printed result:##
def Strings_methods_Task02():
    '''\033[4;33mThis code has:\033[0;33m
    A string type variable named 'string' which is set to "hello world.
    By the .find method, which find the first letter "a" in the variable 'string', it set the variable 'position' to the position of the letter "a" of the string 'string'.
    Then, it print the string 'position' which is, in a nutshell, the position of the first letter "a" in the variable 'string'.\033[0m'''
    string = " hello world "
    position = string . find ("a")
    print ( position )
# help(Strings_methods_Task02)

## Can you predict the result of the following snippet of code? ##
# This code print 2nd before last letter : 'i' here #
def Strings_methods_Task03():
    p = " abcdefghij "
    print ( p [:: -2])
    print( p [:: -2][:5])
    print( p [:: -2][:5][:: -1])
    print (p [:: -2][:5][:: -1][3:])
 
## Can you simplify the previous code? ##
def Strings_methods_Task04():
    p = " abcdefghij "
    print ( p [-3])

## Write a snippet of code that prints 10 times a given string. ##
def Strings_methods_Task05():
    string = input("\033[1;32mWhat do you want to use ? : \033[0m")
    string = "\n"+string
    print("\033[1;33mYour string 10 times : \033[0;34m", string*10,  "\033[0m")

## Rewrite the previous code in as few characters as possible ##
def Strings_methods_Task06(s):
    print(s*10)

## Debug the following code: ##
def Strings_methods_Task07():
    s1 = " Hello "
    s2 = 42
    concat = s1 + str(s2) # replaced '+ s2' by '+ str(s2)'
    print ( concat )

## Complete the following code so that it prints ##
##  The string "42 is the answer" contains 16 characters. ##
def Strings_methods_Task08():
    string1 = "42"
    string2 = " is "
    string3 = "the answer"
    concat = string1+string2+string3
    print ("\033[44mThe string" ,"\""+concat+"\"", "contains", len(concat) ,"characters.\033[0m")
#####

### Strings ###
## Ask the user his/her name and then greet him/her with ##
## “Hello username”. ##
def User_input_Task00():
    name = input("\033[1;32mWhat do your name ? : \033[0m")
    print(f"\033[0;33mHello {name}\033[0m")

## Ask the user his/her name and then greet him/her with ##
## “Hello Username”, with the user’s name always printed with ##
## its first (and only the first) letter capitalized. ##
def User_input_Task01():
    name = input("\033[1;32mWhat do your name ? : \033[0m").capitalize()
    print(f"\033[0;33mHello {name}\033[0m")

## Prompt the user for two numbers and then print ##
## “The sum of the two provided numbers is sum”. ##
def User_input_Task02():
    number1 = float(input("\033[1;32mYour first number : \033[0m"))
    number2 = float(input("\033[1;32mYour second number : \033[0m"))
    print("\033[1;33mThe sum of the two provided numbers is\033[0;34m",number1+number2,"\033[0m")

## Complete the following snippet of code: ##
## ✓ that asks the user for a whole number ; ##
## ✓ and returns <class ’int’>’. ##
def User_input_Task03():
    number = int(input("\033[1;32mEnter a whole number : \033[0m"))
    print("\033[44m",type(number),"\033[0m")

## Write a program that extracts the first word of each sentences ##
## into a string, and then join them to make a new sentence. ##
## For instance, the input : ##
# This is a test. Is it possible to fly? Good things come to those who never give up. #
# should display : This Is Good. #
def User_input_Task04():
    sentences = str(input("\033[1;32mEnter a sentences : \033[0m"))
    sentences_tab = sentences.split()
    new_sentence = sentences_tab[0]
    for word in range(len(sentences_tab)-1):
        if sentences_tab[word].find(".") >= 0 or sentences_tab[word].find("?") >= 0 or sentences_tab[word].find("!") >= 0 :
            new_sentence += f" {sentences_tab[word+1]}"
    new_sentence += "."
    print(f"\033[44m{new_sentence}\033[0m")
#####

### Challenge ###
## Write a snippet of code that counts the number of occurrences ##
## of the strings “Cat”, “Garden” and “Mice” in any string. ##
# thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN
def Challenge():
    match_Cat = "Cat".lower()
    match_Cat_inv = match_Cat[::-1]
    match_Garden = "Garden".lower()
    match_Garden_inv = match_Garden[::-1]
    match_Mice = "Mice".lower()
    match_Mice_inv = match_Mice[::-1]
    count = 0
    sentences = str(input("\033[1;32mEnter a sentences : \033[0m"))
    sentences_lower = sentences.lower()
    sentences_tab = sentences_lower.split()
    for word in range(len(sentences_tab)):
        if sentences_tab[word].find(match_Cat) >= 0 or sentences_tab[word].find(match_Garden) >= 0 or sentences_tab[word].find(match_Mice) >= 0 or sentences_tab[word].find(match_Cat_inv) >= 0 or sentences_tab[word].find(match_Garden_inv) >= 0 or sentences_tab[word].find(match_Mice_inv) >= 0 :
            count += 1
    print(f"\033[1;33m{count}\033[0m")
#####