##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 04, Question 1
##===============================================

import math
import check

## Question 1
# Question1(a)
# powers_plus(n,k,a) returns a list containning the first k powers of n, 
#    starting with the ath power.
# powers_plus: Nat Nat Nat -> (Listof Nat)
# Examples:
# powers_plus(2,3,0) => [1,2,4]
def powers_plus(n,k,a):
    if a == k:
        return []
    else:
        return [n**a] + powers_plus(n,k,a+1)
# powers(n,k) returns a list containning the first k powers of n, starting with
#   the 0th power.
# powers: Nat Nat -> (Listof Nat)
# Examples:
# powers(2,4) => [1,2,4,8]
def powers(n,k):
    return powers_plus(n,k,0)
# Test1: n = 0
check.expect('Q1aT1', powers(0, 3), [1,0,0])
check.expect('Q1aT2', powers(0, 0), [])
# Test2: k = 0
check.expect('Q1aT3', powers(3, 0), [])
# Test3: k != 0 and n != 0
check.expect('Q1aT4', powers(3,4), [1,3,9,27])


# Question1(b)
# count_wins(lst1,lst2) returns the number of times that an element in the lst1
#     is greater than the corresponding element in the lst2
# count_wins: (listof Nat) (listof Nat) -> Nat
# Examples:
# count_wins([1,2,0,4],[4,1,0,2]) => 2
def count_wins(lst1,lst2):
    if lst1[0:] == [] and lst2[0:] == []:
        return 0
    elif  lst1[0] > lst2[0]:
        return 1 + count_wins(lst1[1:], lst2[1:])
    else: 
        return 0 + count_wins(lst1[1:], lst2[1:])
# Test1: lst1 and lst2 equal to []
check.expect('Q1bT1', count_wins([],[]), 0)
# Test2: all lst1 elements greater than lst2
check.expect('Q1bT2', count_wins([5,6,7,8,9], [1,2,3,4,5]), 5)
# Test3: all lst2 elements greater than lst1
check.expect('Q1bT3', count_wins([1,2,3,4,5], [5,6,7,8,9]), 0)
# Test4: Regular Example
check.expect('Q1bT4', count_wins([5,2,8,4,5], [2,6,7,10,-1]), 3)

# Question1(c)
# add_lists_position(lst1, lst2, k) mutates lst1, values in lst1 from k position
#  plus the corresponding values in the lst2. the function return None
# add_lists_position: (listof Int) (listof Int) Nat -> None
# Examples:
# a = [1,5,7], b = [3,4,6]
# add_lists([a],[b],1) => None
# After calling add_lists([a],[b]), a become [1,9,13]
def add_lists_position(lst1,lst2,k):
    if k < len(lst1) or k < len(lst2):
        lst1[k] = lst1[k] + lst2[k]
        add_lists_position(lst1,lst2,k+1)
        
# add_lists(lst1, lst2) mutates lst1, each values in lst1 plus the corresponding
#   values in the lst2. the function return None
# add_lists: (listof Int) (listof Int) -> None
# Examples:
# a = [1,5,7], b = [3,4,6]
# add_lists([a],[b]) => None
# After calling add_lists([a],[b]), a become [4,9,13]
def add_lists(lst1,lst2):
    add_lists_position(lst1,lst2,0)
    
# Test1: Regular Test
a = [1,5,7]
b = [3,4,6]
check.expect('Q1cT1',add_lists(a,b), None)
check.expect('Q1cT1(a)',a, [4,9,13])
# Test2: 
c = [-4,-2]
d = [-1,-3]
check.expect('Q1cT2',add_lists(c,d), None)
check.expect('Q1cT2(a)',c, [-5,-5])
