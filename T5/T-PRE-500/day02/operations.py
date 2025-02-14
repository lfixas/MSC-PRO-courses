### Variables ###
## Compute 1 + 11 + 111 + ... + 111111111 etc... and with power 2, 3, 4, etc... ##
def task01(max,power=1):
    value = 0
    for one in range(1,max+1):
        number = int("1"*one)
        value += number**power
    print("\033[1;36m{0}\033[0m".format(value))

## Computes 17**1024 in less than 10 lines of code ##
def task02(number=17,power=1024):
    result = number
    for add in range (power-1):
        result *= number
    print (result)
#####

### Modulo ###
## Computes the result, as well as both the quotient and the remainder of the euclidean division 42/4 ##
def Task01():
    print(42/4)
    print(42//4)
    print(42%4)

##  check if a number is odd or even ##
def Task02(number):
    result = number%2
    if result == 1 :
        print ("\033[1;36mThe number {0} is \033[4modd\033[0m".format(number))
    else:
        print ("\033[1;32mThe number {0} is \033[4mevent\033[0m".format(number))

## calculates the sum of a digits ##
def Task03(digits=123434565):
    sum = 0
    list_digits = [int(digit) for digit in str(digits)]
    for calculates_sum in list_digits:
        sum += int(calculates_sum)
    print ("\033[1;32m\033[4mResult :\033[0m \033[1;36m{0}\033[0m".format(sum))

## extracts the integer part a number ##
def Task04(numbers):
    print("\033[1;32m\033[4mInteger part of number {0} is :\033[0m \033[1;36m {1}".format(numbers,int(numbers//1)))

## extracts the integer part of a number ##
def Task04_bis1(numbers):
    tab = []
    result = ""
    for digit in str(numbers):
        tab.append(digit)
    for digit_tab in tab:
        if digit_tab == ".":
            result = int(result)
            print(result)
            return
        else :
            result += digit_tab

## extracts the integer part of a number ##
def Task04_bis2(number):
    number_str = str(number)
    for digit in range(1,len(number_str)+1):
        if number_str[-digit] == ".":
            point = digit
    result = []
    for var in range(0,len(number_str)-point): #équivalent à str[:point]
        result.append(number_str[var])
        result2 = "".join(result)
        result2 = int(result2)
    print(result2)

## extracts the decimal part of a number ##
def Task05(number):
    number_str = str(number)
    for digit in range(len(number_str)):
        if number_str[digit] == ".":
            point = digit
    for var in range(1,point):
        result = number_str[point+1:]
        result = int(result)
    print(result)
#####

### Archimedes constant and more ###
## Calculate the first 6 decimals of Pi using the formula : ##
# π = 4x(1/1 − 1/3 + 1/5 − 1/7...) #
import math
def fTask01(denom=1):
    adsu = "+"
    sum = 0
    for divide in range(1,denom+1):
        odd = divide%2
        if odd == 1 :
            div = 1/divide
            if adsu == "+" :
                sum += div
                adsu = "-"
            else :
                sum -= div
                adsu = "+"
    pi = 4*(sum)
    print("pi :", round(pi,6))
    print("math.pi",math.pi)

## Calculate the first 6 decimals of Pi using an amazing formula ##
def fTask02(num): # marcho pô
    list = []
    inverted = []
    numer = 6+6
    for numerator in range(1,num+1):
        odd = numerator%2
        if odd == 1 :
            list.append(numerator)
    for i in range(1,len(list)+1):
        inverted.append(list[-i])
    for n in range(1,len(inverted)):
        numer = 6+(n**2)/numer
    pi = numer-3
    print(pi)
    print(math.pi)

    #pi=3+((1**2)/6+3**2

fTask02(7000)

## Write a program to reduce fractions ##
def fTask03(num):
    pi = 3
    adsu = "+"
    list_numbers = []
    for numbers in range(2,num+1):
        list_numbers.append(numbers)
    print(list_numbers)
    for num in range(len(list_numbers)-2):
        a,b,c = list_numbers[num],list_numbers[num+1],list_numbers[num+2]
        if adsu == "+" :
            pi += 4/(a*b*c)
            adsu = "-"
        else :
            pi -= 4/(a*b*c)
            adsu = "+"
    print("pi :", pi)
    print("pi :", round(pi,6))
    print("math.pi",math.pi)
#####