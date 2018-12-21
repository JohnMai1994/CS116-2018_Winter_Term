##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 04, Question 2
##===============================================

import math
import check

## Question 2
# Question2(a)
# shouting(s) return True if the s contains more Capital Letters than it does
#    lower case letters, else, return False
# shouting: Str -> Bool
# Examples:
# shouting("HELLO World!") => True
def shouting(s):
    if len(list(filter(lambda high: high[:1].isupper(), s))) > \
       len(list(filter(lambda low: low[:1].islower(), s))):
        return True
    else:
        return False
# Test1: string is contain all same type letters
check.expect('Q2aT1', shouting("abcdefg"), False)
check.expect('Q2aT2', shouting("ASFKSD"), True)
check.expect('Q2aT3', shouting("123!@#"), False)
# Test2: Regular example
check.expect('Q2aT4', shouting("AFKLla"), True) 
check.expect('Q2aT5', shouting("AFKLl123a"), True)
check.expect('Q2aT6', shouting("ALl3a"), False)
check.expect('Q2aT7', shouting("AFKL1235"), True)

# Question2(b)
# replace_fun(k, match, rep) return a number, if k is equal to match, then return
#   rep, else return itself
# replace_fun: Int Int Int -> Int
# Examples:
# replace_fun(5, 5, 3) => 3
# replace_fun(5, 6, 3) => 5

def replace_fun(k, match, rep):
    if k == match:
        return rep
    else:
        return k
# replace(lst, match, rep) return a list with same number as lst, but all 
#   occurrences of match will be replaced by rep
# replace: (listof Int) Int Int -> (listof Int)
# Examples:
# replace([1,2,-1,2], 2, 0) => [1,0,-1,0]
def replace(lst,match,rep):
    return list(map(lambda k: replace_fun(k, match, rep), lst))
# Test1: Regular Example
check.expect("Q2bT1", replace([1,2,-1,2], 2, 0), [1,0,-1,0])
check.expect("Q2bT2", replace([1,2,-1,2,4,2], 2, 5), [1,5,-1,5,4,5])
check.expect("Q2bT3", replace([2,2,2,2], 2, 0), [0,0,0,0])
check.expect("Q2bT4", replace([1,3,-1,5], 2, 0), [1,3,-1,5])

# Question2(c)
# keep_quotients(lst,n) return a list that contains the quotients the corresponding
#   elements of lst by n
# keep_quotients: (listof Nat) Nat -> (listof Nat)
# Examples:
# keep_quotients([6,8,7,2], 2) => [3,4,1]
def keep_quotients(lst,n):
    return list(map(lambda l: int(l/n),list(filter(lambda div_2: div_2%n == 0, lst))))
# Test
check.expect('Q2cT1', keep_quotients([6,8,7,2], 2), [3,4,1])
check.expect('Q2cT1', keep_quotients([6,8,9,2,3], 7), [])
check.expect('Q2cT1', keep_quotients([6,8,10,2], 2), [3,4,5,1])
check.expect('Q2cT1', keep_quotients([4,3,7,9,6], 3), [1,3,2])
