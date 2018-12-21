##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 05, Question 1
##===============================================
## Edit the body of each function to use accumulative
## recursion. Don't forget to complete the remainder
## of each design recipe.

import check 
# Question 1 - Part a
# dot_product_acc(alst, blst, num_is_require) returns the sum of Float number, 
#   num_is_require, that an element in alist and multiple the corresponding 
#   element in the blist.
# dot_product_acc: (listof Float) (listof Float) Float -> Float
# requires: len(alst) = len(blst)
# Examples: 
# dot_product_acc([-1.0, 2.0], [2.0, 1.0], 0.0) => 0.0
# dot_product_acc([1.0, 2.0, 3.0], [1.0, 1.0, 1.0], 0.0) => 6.0
def dot_product_acc(alst, blst, num_is_require):
    if len(alst) == 0 or blst == 0:
        return num_is_require
    else:
        num_is_require = num_is_require + (alst[0] * blst[0]) 
        return dot_product_acc(alst[1:], blst[1:], num_is_require)

# dot_product(A, B) returns the sum of Float number that an element in A list 
#   and multiple the corresponding element in the B list
# dot_product: (listof Float) (listof Float) -> Float
# requires: len(A) == len(B)
# Examples:
# dot_product([-1.0, 2.0], [2.0, 1.0]) => 0.0
# dot_product([1.0, 2.0, 3.0], [1.0, 1.0, 1.0]) => 6.0
'''
def dot_product(A, B):
    if len(A) == 0:  # or len(B) == 0:
        return 0.0
    return A[0]*B[0] + dot_product(A[1:], B[1:])
'''

def dot_product(A, B):
    return dot_product_acc(A, B, 0.0)
# Tests:
# Test1: A and B == []
check.expect('Q1aT1', dot_product([],[]), 0.0)
# Test2: Regular Tests
check.expect('Q1aT2', dot_product([-1.0, 2.0],[2.0,1.0]), 0.0)
check.expect('Q1aT3', dot_product([1.0,2.0,3.0], [1.0,1.0,1.0]), 6.0)
check.expect('Q1aT4', dot_product([1.0,6.0,9.0,10.0],[0.0,1.0,2.0,3.0]), 54.0)
# Test3: 
check.expect('Q1aT5', dot_product([-1.5, 2.5],[2.0,1.0]), -0.5)
check.within('Q1aT6', dot_product([1.5,2.0,3.0], [1.0,1.8,-1.0]), 0.00001, 2.1)
check.expect('Q1aT7', dot_product([1.1,2.0],[2.0,-2.1]), -2.0)

# Question 1 - Part b
# keep_positive_acc(lst, list_is_required) returns an list of positive Int, 
#   list_is_required and gets rid of the other negative element in L
# keep_positive_acc: (listof Int) (listof Int) -> (listof Nat)
# Examples:
# keep_positive_acc([1, 2],[]) => [1, 2]
# keep_positive_acc([3, -1, 2, 0, 1],[]) => [3, 2, 1]
def keep_positive_acc(lst, list_is_required):
    if lst == []:
        return list_is_required
    else:
        if lst[0] > 0:
            list_is_required.append(lst[0])
            return keep_positive_acc(lst[1:], list_is_required)
        else:
            return keep_positive_acc(lst[1:], list_is_required)



# keep_positive(L) returns an list of positive Int and gets rid of the other 
#  negative element in L
# keep_positive: (listof Int) -> (listof Nat)
# Examples:
# keep_positive([1, 2]) => [1, 2]
# keep_positive([3, -1, 2, 0, 1]) => [3, 2, 1]
'''
def keep_positive(L):
    return list(filter(lambda x: x>0, L))
'''
def keep_positive(L):
    return keep_positive_acc(L, [])
# Tests:
# Test1: all negative element in L
check.expect("Q1bT1", keep_positive([-1,-2,-5,-10,-1]),[])
check.expect("Q1bT2", keep_positive([-1,-2,-1]),[])
# Test2: including 0 in L
check.expect("Q1bT3", keep_positive([0,0,0,0,0,0]),[])
check.expect("Q1bT4", keep_positive([1,0,3,0,-2,0]),[1,3])
# Test3: Regular Examples
check.expect("Q1bT5", keep_positive([1,-3,2,5,7,-7]),[1,2,5,7])
check.expect("Q1bT6", keep_positive([-1,3,-2,5,-7,0]),[3,5])
check.expect("Q1bT7", keep_positive([0,4,-2,3,8,0]),[4,3,8])
# Test4: empty list
check.expect("Q1bT8", keep_positive([]),[])
