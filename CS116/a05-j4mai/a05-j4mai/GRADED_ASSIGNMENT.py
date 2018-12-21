ASSIGNMENT 05
Student's Quest ID: j4mai

**** Testing Results **********************************************************

31/32   Total Mark

 ** Question 1: 9/9
 ** Question 2: 6/6
 ** Question 3: 8/8
 ** Question 4: 8/9

(Question 1, Test t01, 1 marks): Part A: Orthogonal 2D Vectors: Passed;
    passed.
(Question 1, Test t02, 1 marks): Part A: The all-one vector sums the other
    vector.: Passed; passed.
(Question 1, Test t03, 1 marks): Part A: Base Case: Passed; passed.
(Question 1, Test t04, 1 marks): Part A: More complicated vectors.: Passed;
    passed.
(Question 1, Test t05, 1 marks): Part B: Base Case: Passed; passed.
(Question 1, Test t06, 1 marks): Part B: Keep everything in list of two ele-
    ments: Passed; passed.
(Question 1, Test t07, 1 marks): Part B: Keep most of the elements in a list
    that contains 0.: Passed; passed.
(Question 1, Test t08, 1 marks): Part B: Longer list, keeping everything in-
    cluding 1: Passed; passed.
(Question 1, Test t09, 1 marks): Part B: keeping nothing and excluding 0:
    Passed; passed.
(Question 2, Test t01, 1 marks): Assignment Example 1: Passed; passed.
(Question 2, Test t02, 1 marks): Assignment Example 2: Passed; passed.
(Question 2, Test t03, 1 marks): Base Case: Passed; passed.
(Question 2, Test t04, 1 marks): n = 10: Passed; passed.
(Question 2, Test t05, 1 marks): One of each digit: Passed; passed.
(Question 2, Test t06, 1 marks): Longer complicated number: Passed; passed.
(Question 3, Test t01, 1 marks): Assignment Example 1: Passed; passed.
(Question 3, Test t02, 1 marks): Assignment Example 2: Passed; passed.
(Question 3, Test t03, 1 marks): Base Case: Passed; passed.
(Question 3, Test t04, 1 marks): n = 2: Passed; passed.
(Question 3, Test t05, 1 marks): n = 5: Passed; passed.
(Question 3, Test t06, 1 marks): Harder example: n = 1000: Passed; passed.
(Question 3, Test t07, 1 marks): Longest sequence for n < 1000: Passed;
    passed.
(Question 3, Test t08, 1 marks): Shortest sequence for n > 1000000000: Passed;
    passed.
(Question 4, Test t01, 1 marks): Assignment Example 1: Passed; passed.
(Question 4, Test t02, 1 marks): Assignment Example 2: Passed; passed.
(Question 4, Test t03, 1 marks): Base Case: Passed; passed.
(Question 4, Test t04, 1 marks): Simple two-letter cases: Passed; passed.
(Question 4, Test t05, 1 marks): Medium difficulty three-letter cases: Passed;
    passed.
(Question 4, Test t06, 1 marks): Many characters, all different: Passed;
    passed.
(Question 4, Test t07, 1 marks): Many characters, all the same.: Passed;
    passed.
(Question 4, Test t08, 1 marks): Hard (need to try all possibilities): FAILED;
    FAILED: got [False, False] expected [True, False]
(Question 4, Test t09, 1 marks): Hard (need to try all possibilities): Passed;
    passed.


**** testing_result.txt *****************************************************************
Total number of tests missing: 2

dot_product: All 3 required cases were tested.

keep_positive: All 3 required cases were tested.

count_digits: All 3 required cases were tested.

collatz_number: All 3 required cases were tested.

is_folded: 2 of the 7 required cases were missing:
 - empty strings
 - length of 1



**** a05q1.py *****************************************************************
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

**** a05q2.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 05, Question 2
##===============================================
import check
# Question 2
# count_digits_acc(str_num, list_is_required, start_num) returns a list of 
#   length 10, list_is_required, where the start_numth element of the list 
#   contains the number of times that the digit start_num occurs in star_num
# count_digits_acc: Str (listof Nat) Nat -> (listof Nat)
# Examples:
# count_digits_acc('440222', [], 0) => [1, 0, 3, 0, 2, 0, 0, 0, 0, 0]
# count_digits('973195', [], 0) => [0, 1, 0, 1, 0, 1, 0, 1, 0, 2]
def count_digits_acc(str_num, list_is_required, start_num):
  if start_num > 9:
    return list_is_required
  else:
    list_is_required.append(str_num.count(str(start_num)))
    return count_digits_acc(str_num, list_is_required, start_num+1)

# count_digits(n) returns the count of each digit in n
# count_digits: Nat -> (listof Nat)
# Examples:
# count_digits(440222) => [1, 0, 3, 0, 2, 0, 0, 0, 0, 0]
# count_digits(973195) => [0, 1, 0, 1, 0, 1, 0, 1, 0, 2]
def count_digits(n):
  string = str(n)
  return count_digits_acc(string, [], 0)
# Test:
# Test1: n = 0
check.expect('Q2T1', count_digits(0), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# Test2: number from 0-9 happen
check.expect('Q2T2', count_digits(1234567890), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
check.expect('Q2T3', count_digits(1234567312890), [1, 2, 2, 2, 1, 1, 1, 1, 1, 1])
check.expect('Q2T4', count_digits(12233445567312890), [1, 2, 3, 3, 2, 2, 1, 1, 1, 1])
# Test3: some number happen more than 2 times
check.expect('Q2T5', count_digits(1789789789789), [0, 1, 0, 0, 0, 0, 0, 4, 4, 4])
check.expect('Q2T6', count_digits(1578682457), [0, 1, 1, 0, 1, 2, 1, 2, 2, 0])
# Test4: only one number exist
check.expect('Q2T7', count_digits(999999), [0, 0, 0, 0, 0, 0, 0, 0, 0, 6])
check.expect('Q2T8', count_digits(111111), [0, 6, 0, 0, 0, 0, 0, 0, 0, 0])
check.expect('Q2T9', count_digits(000000), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])


**** a05q3.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 05, Question 3
##===============================================
import check

# Question 3
# collatz_number_acc(list_of_need) returns the list of positive integer in the 
# 3n + 1 sequence beginning with the first element of list_of_need
# collatz_number_acc: (listof Int) -> (listof Int)
# Requires:
# the element in the list_of_need > 0
# Examples:
# collatz_number_acc([3]) => [3, 10, 5, 16, 8, 4, 2, 1]
# collatz_number_acc([4,2]) => [4, 2, 1]
def collatz_number_acc(list_of_need):
  if list_of_need[-1] == 1:
    return list_of_need
  else:
    if list_of_need[-1]%2 == 1:
      list_of_need.append(int(list_of_need[-1]*3+1))
      return collatz_number_acc(list_of_need)
    else:
      list_of_need.append(int(list_of_need[-1]/2))
      return collatz_number_acc(list_of_need)
    
# collatz_number(n) returns the number of elements in the 3n + 1 sequence 
#   beginning with n
# collatz_number: Int -> Int
# Requires:
#   n > 0
# Examples:
# collatz_number(3) => 8
# collatz_number(5) => 6
def collatz_number(n):
  return len(collatz_number_acc([n]))
# Test:
# test1: n from 1 to 10
check.expect('Q3T1', collatz_number(1), 1)
check.expect('Q3T2', collatz_number(2), 2)
check.expect('Q3T3', collatz_number(3), 8)
check.expect('Q3T4', collatz_number(4), 3)
check.expect('Q3T5', collatz_number(5), 6)
check.expect('Q3T6', collatz_number(6), 9)
check.expect('Q3T7', collatz_number(7), 17)
check.expect('Q3T8', collatz_number(8), 4)
check.expect('Q3T9', collatz_number(9), 20)
check.expect('Q3T10', collatz_number(10), 7)
# test2: some special number
check.expect('Q3T11', collatz_number(13), 10)
check.expect('Q3T12', collatz_number(17), 13)
check.expect('Q3T13', collatz_number(26), 11)
check.expect('Q3T14', collatz_number(37), 22)
check.expect('Q3T15', collatz_number(47), 105)
check.expect('Q3T16', collatz_number(73), 116)
check.expect('Q3T17', collatz_number(101), 26)

**** a05q4.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 05, Question 4
##===============================================
import check

# Question 4
# is_folded(old, new) returns True if old could be 'folded' into new, otherwise,
#   False.
# is_folded: Str Str -> Bool
# Require:
# len(old) == len(new) and 
# neither len(old) or len(new) exceed 10
# Examples:
# is_folded('AACTC', 'ACATC') => True
# is_folded('ATGCA', 'ACTGA') => False
def is_folded(old, new):
  new_two = new[:2]
  if old == new:
    return True
  else:
    if old[0:2] == new_two:
      return is_folded(old[1:],new[1:])
    elif old[-1]+ old[-2] == new_two:
      return is_folded(old[:-1], new[1:])
    elif old[0] + old[-1] == new_two:
      return is_folded(old[1:], new[1:])
    elif old[-1] + old[0] == new_two:
      return is_folded(old[:-1], new[1:])
    else:
      return False
# Tests:
# Test1: Example Test:
check.expect('Q4T1', is_folded('AACTC', 'ACATC'), True)
check.expect('Q4T2', is_folded('ATGCA', 'ACTGA'), False)
# Test2: start -> start -> start:
check.expect('Q4T3', is_folded('AACTC', 'AACTC'), True)
check.expect('Q4T4', is_folded('AACTCABRQE', 'AACTCABRQE'), True)
check.expect('Q4T5', is_folded('AACTC', 'ACCTA'), False)
# Test3: end -> end ->end:
check.expect('Q4T6', is_folded('AACTC', 'CTCAA'), True)
check.expect('Q4T7', is_folded('AACTCATC', 'CTACTCAA'), True)
check.expect('Q4T8', is_folded('AACTCATC', 'CTACCTAA'), False)
# Test4: start -> end -> start:
check.expect('Q4T9', is_folded('AACTCATC', 'ACATCATC'), True)
check.expect('Q4T10', is_folded('ATGCAWEIR', 'ARTIGECWA'), True)
check.expect('Q4T11', is_folded('ATGCA', 'AATCG'), True)
check.expect('Q4T12', is_folded('ATGCA', 'AAGTC'), False)
# Test5: start -> end -> end -> start:
check.expect('Q4T13', is_folded('ATGCA', 'AACTG'), True)
check.expect('Q4T14', is_folded('AACTC', 'ACTAC'), True)
check.expect('Q4T15', is_folded('AACTCATC', 'ACTACACT'), True)


**** End of graded assignment. *************************************************
