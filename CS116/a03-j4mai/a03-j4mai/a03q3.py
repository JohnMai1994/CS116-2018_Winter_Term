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
