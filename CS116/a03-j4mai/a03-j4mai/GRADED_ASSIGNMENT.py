ASSIGNMENT 03
Student's Quest ID: j4mai

**** Testing Results **********************************************************

29/29   Total Mark

 ** Question 1: 8/8
 ** Question 2: 6/6
 ** Question 3: 7/7
 ** Question 4: 8/8

(Question 1, Test t01, 1 marks): missing >1 condition, with >1 repeat: Passed;
    passed.
(Question 1, Test t02, 1 marks): includes space: Passed; passed.
(Question 1, Test t03, 1 marks): missing number, no repeat: Passed; passed.
(Question 1, Test t04, 1 marks): missing uppercase, no repeat: Passed; passed.
(Question 1, Test t05, 1 marks): missing lowercase, no repeat: Passed; passed.
(Question 1, Test t06, 1 marks): no prompt repeat, multiple digits and let-
    ters: Passed; passed.
(Question 1, Test t07, 1 marks): 1 condition missing, >1 repeat: Passed;
    passed.
(Question 1, Test t08, 1 marks): non alphanumeric test: Passed; passed.
(Question 2, Test t01, 1 marks): Q2:test 1: Passed; passed.
(Question 2, Test t02, 1 marks): Q2:test 2: Passed; passed.
(Question 2, Test t03, 1 marks): Q2:test 3: Passed; passed.
(Question 2, Test t04, 1 marks): Q2:test 4: Passed; passed.
(Question 2, Test t05, 1 marks): Q2:test 5: Passed; passed.
(Question 2, Test t06, 1 marks): Q2:test 6: Passed; passed.
(Question 3, Test t01, 1 marks): no mistake: Passed; passed.
(Question 3, Test t02, 1 marks): mistake at the 2nd step: Passed; passed.
(Question 3, Test t03, 1 marks): mistake at the 3rd step: Passed; passed.
(Question 3, Test t04, 1 marks): mistake at the 4th step: Passed; passed.
(Question 3, Test t05, 1 marks): mistake at the 5th step: Passed; passed.
(Question 3, Test t06, 1 marks): multiple repetition at any step: Passed;
    passed.
(Question 3, Test t07, 1 marks): testing zero: Passed; passed.
(Question 4, Test t01, 1 marks): smallest inputs: Passed; passed.
(Question 4, Test t02, 1 marks): 1 line split, uneven finish: Passed; passed.
(Question 4, Test t03, 1 marks): n > words in s: Passed; passed.
(Question 4, Test t04, 1 marks): all lines same length: Passed; passed.
(Question 4, Test t05, 1 marks): single word: Passed; passed.
(Question 4, Test t06, 1 marks): n == number of words: Passed; passed.
(Question 4, Test t07, 1 marks): more than 2 lines, uneven finish: Passed;
    passed.
(Question 4, Test t08, 1 marks): 1 word per line: Passed; passed.


**** testing_result.txt *****************************************************************
Total number of tests missing: 10

pass_check: 3 of the 8 required cases were missing:
 - exactly one invalid input
 - includes space
 - includes non alphanumeric

bin2nat: 1 of the 4 required cases were missing:
 - bistr='0'

number_game: 3 of the 6 required cases were missing:
 - mistake - 3rd step
 - mistake - last step
 - repeated mistake - any step

make_poem: 3 of the 6 required cases were missing:
 - len(s)=1
 - n > number of words in s
 - n=number of words



**** a03q1.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 03, Question 1
##===============================================

import check

# Q1

invalid_msg = "Invalid password"
end_msg = "Thank you!"
welcome_msg = "Enter a password:"

# contain_num(a,n) return True if a contain a number from n position, return 
#    False if a not contain a number from n position 
# contain_num: Str Int -> Bool
# Examples:
# contain_num("abB3", 0) => True
# contain_num("abc", 0) => False
def contain_num(a,n):
    if n == len(a): 
        return False
    if a[n:n+1].isnumeric():
        return True
    else:
        return contain_num(a, n+1)
# contain_lower(b,n) return True if b contain a lower-case from n position, return 
#    False if b not contain a lower-case from n position 
# contain_lower: Str Int -> Bool
# Examples:
# contain_lower("abB3", 0) => True
# contain_lower("AB213", 0) => False
def contain_lower(b,n):
    if n == len(b):
        return False
    if b[n:n+1].islower():
        return True
    else:
        return contain_lower(b, n+1)        
# contain_upper(c,n) return True if c contain a upper-case from n position, return 
#    False if c not contain a upper-case from n position 
# contain_upper: Str Int -> Bool
# Examples:
# contain_upper("abB3", 0) => True
# contain_upper("abc34", 0) => False
def contain_upper(c,n): 
    if n == len(c):
        return False
    if c[n:n+1].isupper():
        return True
    else:
        return contain_upper(c, n+1)     
# contain_space(d,n) return True if d contain a space from n position, return 
#    False if d not contain a space from n position 
# contain_space: Str Int -> Bool
# Examples:
# contain_space("abB 3", 0) => True
# contain_space("abc", 0) => False
def contain_space(d,n):
    if n == len(d):
        return False
    if d[n:n+1].isspace():
        return True
    else:
        return contain_space(d,n+1)
# valid_password(myp,n) return True if myp is a valid password, contain a number,
#   an upper-case, a lower-case and no space, else return False
# valid_password: str Int -> Bool
# Examples:
# valid_password("aB12C",0) => True
# valid_password("aB 12C",0) => False
def valid_password(myp,n):
    if contain_lower(myp,n) and contain_num(myp,n) and contain_upper(myp,n) and\
       not(contain_space(myp,n)):
        return True
    else:
        return False

# pass_check() get the password(myp) from the user. If the password is 
#   considered valid, print "Thank you!" and return the password(myp). If
#   the password is invalid, print "Invalid password".
# Effects: Prints promopts to the user and reads in the password, prints out 
#    'Thank you!', if password is valid. prints out 'Invalid password', if 
#    password is invalid
# pass_check: None -> Str
# Examples:
# If the user enters 'hi there' when pass_check() is called, prints 
#   'Invalid password'
# If the user enters 'boB35' when pass_check() is called, prints 'Thank you!'
#   and 'boB35' is returned
def pass_check():
    my_password = str(input(welcome_msg))
    if valid_password(my_password, 0):
        print(end_msg)
        return my_password
    else:
        print(invalid_msg)
        return pass_check()
    
# Test Valid password
check.set_input(["Ab3"])
check.set_screen("Thank you!")
check.expect("Q1T1", pass_check(), "Ab3")

# Test Invalid password, only contain number, lower-case or upper-case
check.set_input(["abc", "123", "ABC","Af3"])
check.set_screen("Invalid password\nInvalid password\nInvalid password\nThank you!")
check.expect("Q1T2", pass_check(), "Af3")

# Test Invalid password, contain two of number, lower-case or upper-case
check.set_input(["af3", "afFFG", "AF346", "AFfe3"])
check.set_screen("Invalid password\nInvalid password\nInvalid password\nThank you!")
check.expect("Q1T3", pass_check(), "AFfe3")



**** a03q2.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 03, Question 2
##===============================================

import check

# Q2
# bin2nat(bistr) returns a natural number representing the decimal value of 
#    bistr
# bin2nat: Str -> Nat
# Requires:
# Bistr is a non-empty string only contain "0" and "1"
# Examples:
# bin2nat("101") => 5
# bin2nat("1111") => 15

def bin2nat(bistr):
    mul_times = len(bistr) -1
    if mul_times == -1:
        return 0
    else:
        num = int(bistr[0:1])
    return num*(2**mul_times) + bin2nat(bistr[1:])

# Test1: all 0
check.expect("Q2Test1", bin2nat("000000"), 0)
# Test2: all 1
check.expect("Q2Test2", bin2nat("1"), 1)
check.expect("Q2Test3", bin2nat("11"), 3)
check.expect("Q2Test4", bin2nat("111"), 7)
check.expect("Q2Test5", bin2nat("1111"), 15)
# Test3: contain 1 and 0
check.expect("Q2Test6", bin2nat("101"), 5)
check.expect("Q2Test7", bin2nat("1011"), 11)
check.expect("Q2Test8", bin2nat("1010101"), 85)

**** a03q3.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 03, Question 3
##===============================================

import check

# Q3

error_msg = 'That is not correct.'
step1_msg = 'Think of a number. Multiply your number by 4:'
step2_msg = 'Add 9:'
step3_msg = 'Subtract the original number:'
step4_msg = 'Divide by 3:'
step5_msg = 'Subtract 3:'
final_msg = 'Your original number is {0}'

# plus_9(s) ask the user for a number that is equal to s plus 9, until get a 
#   correct answer from the user
# Effects: reads input from user
# plus_9: Int -> Int
# Examples:
# If the user input is 49, plus_9(40) => 49
# If the user input is 48, puls_9(40) prints "That is not correct." and repeat
#   the question again
def plus_9(s):
    k = int(input(step2_msg))
    if k == s + 9:
        return k
    else:
        print(error_msg)
        return plus_9(s)
    
# sub_ori(a,c) ask the user for a number that is equal to a minus c, until get a 
#   correct answer from the user
# Effects: reads input from user
# sub_ori: Int Int -> Int
# Examples:
# If the user input is 39, sub_ori(49,10) => 39
# If the user input is 40, sub_ori(49,10) prints "That is not correct." and repeat
#   the question again
def sub_ori(a, c):
    b = int(input(step3_msg))
    if b == a - c:
        return b
    else:
        print(error_msg)
        return sub_ori(a,c)
    
# div_3(d) ask the user for a number that is equal to d divide 3, until get a 
#   correct answer from the user
# Effects: reads input from user
# div_3: Int -> Int
# Examples:
# If the user input is 13, div_3(39) => 13
# If the user input is 12, div_3(39) prints "That is not correct." and repeat
#   the question again   
def div_3(d):
    e = int(input(step4_msg))
    if e == d/ 3:
        return e
    else:
        print(error_msg)
        return div_3(d)
    
# sub_3(f) ask the user for a number that is equal to f minus 3, until get a 
#   correct answer from the user
# Effects: reads input from user
# sub_3: Int -> Int
# Examples:
# If the user input is 10, sub_3(13) => 10
# If the user input is 12, sub_3(13) prints "That is not correct." and repeat
#   the question again      
def sub_3(f):
    g = int(input(step5_msg))
    if g == f-3:
        return g
    else:
        print(error_msg)
        return sub_3(f)

# number_game() prompts the user choosing a number, reads in a series of 
#   integers. the function prints out a message with the number that user  
#   chosed at the beginning
# Effects: prints promts to the user and reads in a series of integers, prints
#          out a message with the original number that the user chosed
# number_game: None -> None
# Examples:
# If the user input is ["40" "49" "39" "13" "10"], number_game() prints "Your 
#   original number is 10"
def number_game():
    mul_4 = int(input(step1_msg))
    my_num = mul_4/4
    subtract_ori = plus_9(mul_4)
    divide_3 = sub_ori(subtract_ori, my_num)
    subtract_3 = div_3(divide_3)
    final_num = sub_3(subtract_3)
    print(final_msg.format(final_num))
    

# original number = 10
check.set_input(["40", "49", "39", "13", "10"])
check.set_screen("Your original number is 10")
check.expect("original number = 10", number_game(), None)

# original number = 7
check.set_input(["28", "32", "37", "30", "10", "7"])
check.set_screen("Think of a number. Multiply your number by 4:"
                 "Add 9:"
                 "That is not correct"
                 "Subtract the original number:"
                 "Divide by 3:"
                 "Your original number is 7")
check.expect("original number = 7", number_game(), None)

# original number = 1
check.set_input(["4", "13", "12", "3", "4", "1"])
check.set_screen("Think of a number. Multiply your number by 4:"
                 "Add 9:"
                 "Subtract the original number:"
                 "Divide by 3:"
                 "That is not correct."
                 "Your original number is 1")
check.expect("original number = 1", number_game(), None)    


**** a03q4.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 03, Question 4
##===============================================

import check

#Q4
# space_position(s, n) consumes a string, s, and a natural number, n, and returns
#   an number n space position in s.
# space_position: Str Nat -> Nat
# Requires:
# s is a non-empty string
# n is a natural number greater than 0
# Examples:
# space_position("ab ab ar cde fa e", 3) => 8

def space_position(s, n):
    g = 0
    if n == 0:
        return -1
    if s[0:1].isspace():
        g = 1 + space_position(s[1:], n-1) 
    else:
        if s.count(" ") >= n:
            g = 1 + space_position(s[1:], n)
        else:
            g = len(s) +1 
    return g


# make_poem(s,n) consumes a string, s, and a natural number, n, and prints out
#  multiple lines, the same string as s where each line has n words in it.
# make_poem: Str Nat -> None
# Requires:
# s is a non-empty string
# n is a natural number greater than 0
# Examples:
# make_poem("How many Lowes would Rob Lowe rob if Rob Lowe could rob Lowes", 3) 
#           will print:
#  How many Lowes
#  would Rob Lowe
#  rob if Rob
#  Lowe could rob
#  Lowes
def make_poem(s,n):
    k = space_position(s, n)
    if k >= len(s):
        print(s)
    else:
        print(s[0:k])
        make_poem(s[k+1:], n)

# Test Example, n = 3
check.set_screen("How many Lowes\nwould Rob Lowe\nrob if Rob\nLowe could rob\nLowes")
check.expect("Q4T1", make_poem("How many Lowes would Rob Lowe rob if Rob Lowe could rob Lowes", 3), 
             None)

# Test when n = 1
check.set_screen("abc\ndef\nhijk\nlmno\npQ")
check.expect("Q4T2", make_poem("abc def hijk lmno pQ",1), None)

# Test When n = 4
check.set_screen("my job is very\nawaresome and my dad\nis superman")
check.expect("Q4T3", make_poem("my job is very awaresome and my dad is superman", 4), None)



**** End of graded assignment. *************************************************
