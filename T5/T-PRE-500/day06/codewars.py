### Coloured Triangles ###
row= 'RBRGBRBGGRRRBGBBBGG'
'''def triangle(row):
    new_row = []
    # print(row)
    if len(row) == 1:
        # print(row[0])
        return row[0]
    for color in range(len(row)-1):
        if row[color] == row[color+1]:
            new_row.append(row[color])
        if row[color] == "B" and row[color+1] == "G" or row[color] == "G" and row[color+1] == "B":
            new_row.append("R")
        if row[color] == "R" and row[color+1] == "G" or row[color] == "G" and row[color+1] == "R":
            new_row.append("B")
        if row[color] == "B" and row[color+1] == "R" or row[color] == "R" and row[color+1] == "B":
            new_row.append("G")
    triangle(new_row)'''

def triangle(row):
    new_row = []
    # print(row)
    if len(row) == 1:
        print(row[0])
        return row[0]
    while len(row) != 1: 
        for color in range(len(row)-1):
            if row[color] == row[color+1]:
                new_row.append(row[color])
            if row[color] == "B" and row[color+1] == "G" or row[color] == "G" and row[color+1] == "B":
                new_row.append("R")
            if row[color] == "R" and row[color+1] == "G" or row[color] == "G" and row[color+1] == "R":
                new_row.append("B")
            if row[color] == "B" and row[color+1] == "R" or row[color] == "R" and row[color+1] == "B":
                new_row.append("G")
        row = new_row
        new_row = []
    # print(row[0])
    return row[0]

# triangle('GB') # R
# triangle('RRR') # R
# triangle('RGBG') # B
# triangle('RBRGBRB') # G
# triangle('RBRGBRBGGRRRBGBBBGG') #G
# triangle('B') # B
# triangle(row)

### SevenAte9 ###
def seven_ate9(str_):
    new_str_ = list(str_)
    print(new_str_)
    for str in range(1,len(str_)-1):
        if str_[str] == "9":
            if str_[str-1] == "7" and str_[str+1] == "7":
                new_str_[str] = "X"
    new_str_ = "".join([x for x in new_str_ if x != "X"])
    print(new_str_)
    return new_str_


# seven_ate9("79712312") # "7712312"
# seven_ate9("79797") # "777"

### Determine if the poker hand is flush ###
def is_flush(cards):
    return cards[0][-1] ==  cards[1][-1] == cards[2][-1] == cards[3][-1] == cards[4][-1]

# is_flush(["AS", "3S", "9S", "KS", "4S"]) # True
# is_flush(["AD", "4S", "7H", "KC", "5S"]) # False
# is_flush(["AD", "4S", "10H", "KC", "5S"]) # False
# is_flush(["QD", "4D", "10D", "KD", "5D"]) # True

### Unique Pairs ###
import math
def projectPartners(n):
    if n < 2:
        return 0 
    num_pairs = math.factorial(n) // (2 * math.factorial(n - 2))
    print(num_pairs)
    return num_pairs

# projectPartners(2) # 1
# projectPartners(3) # 3
# projectPartners(4) # 6
# projectPartners(5) # 10

### Unique Sum ###
def unique_sum(lst):
    if len(lst) < 1:
        return None
    new_lst = list(set(lst))
    return sum(ele for ele in new_lst)

# unique_sum([1,2,3]) # 6
# unique_sum([1,3,8,1,8]) # 12
# unique_sum([-1,-1,5,2,-7]) # -1

### Negation of a Value ###
def negation_value(s, val):
    return not val if len(s) % 2 == 1 else not not val

negation_value("!", False) # True
negation_value("!", True) # False

picture_box = ""
#   _____ #
#   |/  | #
#   |   o #
#   |  /|\#
#   |   /\#
#   |     #
# __I__   #

#     o/
#    /|
#    /\




print(picture_box)