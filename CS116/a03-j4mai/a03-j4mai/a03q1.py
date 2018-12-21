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

