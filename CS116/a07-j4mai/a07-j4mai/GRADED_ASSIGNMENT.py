ASSIGNMENT 07
Student's Quest ID: j4mai

**** Testing Results **********************************************************

37/41   Total Mark

 ** Question 1: 6/6
 ** Question 2: 7/7
 ** Question 3: 12/16
 ** Question 4: 12/12

(Question 1, Test t01, 1 marks): Question 1a: Passed; passed.
(Question 1, Test t02, 1 marks): Question 1b: Passed; passed.
(Question 1, Test t03, 1 marks): Question 1c: Passed; passed.
(Question 1, Test t04, 1 marks): Question 1d: Passed; passed.
(Question 1, Test t05, 1 marks): Question 1e: Passed; passed.
(Question 1, Test t06, 1 marks): Question 1f: Passed; passed.
(Question 2, Test t01, 1 marks): simple increasing test: Passed; passed.
(Question 2, Test t02, 1 marks): simple flat and increasing test: Passed;
    passed.
(Question 2, Test t03, 1 marks): decreasing test: Passed; passed.
(Question 2, Test t04, 1 marks): length of 1: Passed; passed.
(Question 2, Test t05, 1 marks): empty list: Passed; passed.
(Question 2, Test t06, 1 marks): short list and more than one increasing se-
    quences: Passed; passed.
(Question 2, Test t07, 1 marks): long list and more than one increasing se-
    quences: Passed; passed.
(Question 3, Test t01, 1 marks): simple tests:one binary search: Passed;
    passed.
(Question 3, Test t02, 1 marks): simple tests:no binary search: Passed;
    passed.
(Question 3, Test t03, 1 marks): simple tests:not exist:binary search: FAILED;
    FAILED: got (['Galloping search from index 0', 'Galloping search from in-
    dex 1', 'Galloping search from index 3'], False) expected (['Galloping
    search from index 0', 'Galloping search from index 1', 'Galloping search
    from index 3', 'Binary search from index 2 to 2'], False)
(Question 3, Test t04, 1 marks): longer list:binary search: Passed; passed.
(Question 3, Test t05, 1 marks): longer list:not exist;last elemnt: Passed;
    passed.
(Question 3, Test t06, 1 marks): longer list:not exist;one binary search:
    FAILED; FAILED: got (['Galloping search from index 0', 'Galloping search
    from index 1', 'Galloping search from index 3', 'Galloping search from in-
    dex 7', 'Galloping search from index 9'], False) expected (['Galloping
    search from index 0', 'Galloping search from index 1', 'Galloping search
    from index 3', 'Galloping search from index 7', 'Galloping search from in-
    dex 9', 'Binary search from index 8 to 8'], False)
(Question 3, Test t07, 1 marks): longer list:one binary search: FAILED;
    FAILED: got (['Galloping search from index 0', 'Galloping search from in-
    dex 1', 'Galloping search from index 3', 'Galloping search from index 7',
    'Binary search from index 8 to 9'], 8) expected (['Galloping search from
    index 0', 'Galloping search from index 1', 'Galloping search from index
    3', 'Galloping search from index 7', 'Galloping search from index 9', 'Bi-
    nary search from index 8 to 8'], 8)
(Question 3, Test t08, 1 marks): length of list is 1,exist: Passed; passed.
(Question 3, Test t09, 1 marks): length of list is 1,not exist: Passed;
    passed.
(Question 3, Test t10, 1 marks): length of list is 2,not exist: Passed;
    passed.
(Question 3, Test t11, 1 marks): length of list is 3,not exist: Passed;
    passed.
(Question 3, Test t12, 1 marks): length of list is 3,exist: Passed; passed.
(Question 3, Test t13, 1 marks): long list;binary search on the first half:
    Passed; passed.
(Question 3, Test t14, 1 marks): long list;binary search on the latter half:
    FAILED; FAILED: got (['Galloping search from index 0', 'Galloping search
    from index 1', 'Galloping search from index 3', 'Galloping search from in-
    dex 7', 'Binary search from index 8 to 13'], 12) expected (['Galloping
    search from index 0', 'Galloping search from index 1', 'Galloping search
    from index 3', 'Galloping search from index 7', 'Galloping search from in-
    dex 14', 'Binary search from index 8 to 13'], 12)
(Question 3, Test t15, 1 marks): first element is greater than the target:
    Passed; passed.
(Question 3, Test t16, 1 marks): longer list:not exist;no binary search:
    Passed; passed.
(Question 4, Test t01, 1 marks): part a:empty list: Passed; passed.
(Question 4, Test t02, 1 marks): part a: only one element in the lst: Passed;
    passed.
(Question 4, Test t03, 1 marks): part a: first lst is empty but the other lsts
    are not: Passed; passed.
(Question 4, Test t04, 1 marks): part a: last lst is empty but the other lsts
    are not: Passed; passed.
(Question 4, Test t05, 1 marks): part a: last lst is empty but the other lsts
    are not: Passed; passed.
(Question 4, Test t06, 1 marks): part a: hard test long list and large number:
    Passed; passed.
(Question 4, Test t07, 1 marks): part b: length of list is 0: Passed; passed.
(Question 4, Test t08, 1 marks): part b: length of list is 1: Passed; passed.
(Question 4, Test t09, 1 marks): part b: length of list is 2: Passed; passed.
(Question 4, Test t10, 1 marks): part b: length of list is 3: Passed; passed.
(Question 4, Test t11, 1 marks): part b: length of list is 5: Passed; passed.
(Question 4, Test t12, 1 marks): part b: long list: Passed; passed.


**** testing_result.txt *****************************************************************
Total number of tests missing: 3

count_longest_asc: 1 of the 6 required cases were missing:
 - len(L) > 1 and list contains only one number repeated

galloping_search: All 4 required cases were tested.

merge3: 2 of the 5 required cases were missing:
 - L1 empty, L2 & L3 non-empty
 - L2 empty, L1 & L3 non-empty

mergesort3: All 5 required cases were tested.



**** a07q1.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 07, Question 1
##===============================================

## Make sure to follow question 1 as directed.

# Question 1. 
#
# Determine the worst-case runtime of the following functions. 
# The answer will be stated in terms of the size of the problem.
# Some bounds may appear more than once.
#
# Note. In all cases, choose the 'tightest' bound.
#
# Choose 
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

# (a)
# Let n = len(L)
def fn_a(L):
    def helper(M, m):
        n = 0  # O(1)
        for x in M:  # n cycle
            if x == m: # O(1)
                n = n + 1 # O(1)
        return n # O(1)
    L1 = list(filter(lambda x: x > helper(L, x), L)) # n* O(n) => O(n^2)
    return len(L1) # O(1)

# (b)
# let n = len(s), c is a string of length 1
def fn_b(s, c):
    if s[0] == c or s[-1] == c: # O(1)
        print('The begins or ends with {0}'.format(c)) # O(1)

# (c)
# n is a natural number
def fn_c(n):
    if n == 0: # O(1)
        return 1 # O(1)
    elif n % 2 == 0:  # O(1)
        return fn_c(n - 1) + fn_c(n - 1) ** 2 # 2T(n-1) 
    else:
        return 2 * fn_c(n - 1) # 2T(n-1)

# (d)
# let n = len(L)
def fn_d(L, x):
    for i in range(len(L)): # n cycle
        j = i    # O(1)
        while j < len(L): # n cycle
            if L[i] + L[j] == x:  #O(1)
                return i + j # O(1)
            j = j + 1 # O(1)
            return -1 # O(1)

# (e)
# let n = len(s)
def fn_e(s):
    s1 = list(filter(lambda c: c.isdigit(), s))  # O(n)
    s2 = list(filter(lambda c: c.isupper(), s))  # O(n)
    s3 = list(filter(lambda c: c.islower(), s))  # O(n)
  
    return s1 + s2 + s3  # O(1)

# (f)
# let n = len(L)
def fn_f(L):
    def helper(M, n):
        m = n // 2 # O(1)
        if n >= len(M): # O(1)
            return 1 # O(1)
        if M[n] > M[0]: # O(1)
            return M[0] + helper(M, m) # O(1) + T(n/2) 
        return M[0] + M[n] # O(1)
    return helper(L, len(L) - 1) # T(n)

# Place one of A,B,C,D,E or F inside the string quotes;
#e.g., if you think fn_a has a running time of O(2**n),
#then change a_answer = "" to a_answer = "F".
#
# Choose:
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

a_answer = "E"
b_answer = "A"
c_answer = "F"
d_answer = "E"
e_answer = "C"
f_answer = "B"

**** a07q2.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 07, Question 2
##===============================================
import check
# Question 2
# count_longest_asc(L) consumes a list of intergers, L, and returns the 
#   the length of the longest run of ascending numbers in the list
# count_longest_asc: (listof Int) -> Int
# Requires:
#   function cannot use recursion
#   function must go through the list exactly once
#   cannot create any new lists
# Examples:
# count_longest_asc([9, 1, 7, 8, 9, 4, 2]) => 4
# count_longest_asc([6, 4, 4, 2]) => 1

def count_longest_asc(L):
    if L == []:
        return 0
    if len(L) == 1:
        return 1
    i = 0
    j = 1
    k = []
    while i+1 < len(L):
        if L[i] < L[min(i+1, len(L))]:
            i += 1
            j += 1
            k.append(j)
        else:
            i += 1
            j = 1
            k.append(j)
    return max(k)



# Test:
# Test1: Examples
l = [9,1,7,8,9,4,2]
check.expect('E1', count_longest_asc(l), 4)
check.expect('E2', count_longest_asc([6,4,4,2]), 1)
# Test2: Only increasing list
check.expect('Q2T1', count_longest_asc([1,3,4,5,6]), 5)
check.expect('Q2T2', count_longest_asc([1,6]), 2)
check.expect('Q2T3', count_longest_asc([1,2,3,4,5,6,8,100]), 8)
# Test3: Only one element in list
check.expect('Q2T4', count_longest_asc([1]), 1)
check.expect('Q2T5', count_longest_asc([]), 0)
check.expect('Q2T6', count_longest_asc([96]), 1)
# Test4: Only decreasing list
check.expect('Q2T7', count_longest_asc([9,8,7,6]), 1)
check.expect('Q2T8', count_longest_asc([15,9,5,3,2,1]), 1)
check.expect('Q2T9', count_longest_asc([10,9,8,7,6,5,4,3,2,1,0]), 1)
# Test5: Mix list 
check.expect('Q2T10', count_longest_asc([1,3,4,5,3,4,2,8,6]), 4)
check.expect('Q2T11', count_longest_asc([1,3,4,5,6,2,1,3,4,5]), 5)
check.expect('Q2T12', count_longest_asc([1,3,2,4,8,5,6]), 3)

**** a07q3.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 07, Question 3
##===============================================
import check
# Question 3
# Note: For *the binary_search function only* you can change
# the design recipe and implementation as required (you will need to)
# in order to adapt the function for your solution to Q3

# binary_search(L, target) returns True if target is
# in L and False otherwise
# binary_search: (listof Int) Int -> Bool
def binary_search(L, target):
    beginning = 0
    end = len(L) - 1
    while beginning <= end:
        middle = beginning + (end - beginning) // 2
        if L[middle] == target:
            return True
        elif L[middle] > target:
            end = middle - 1
        else:
            beginning = middle + 1
    return False

# galloping_search(n, L): consumes a number, n, and a non-empty sorted list
#    of natural number, L, and returns the index of the element or Fase. And
#    print message where the index star from
# galloping_search: Int (listof Int) -> False or Int
# Examples:
# galloping_search(14, [1, 2, 5, 7, 9, 14, 15, 23, 29]) => 5
#   and prints 'Galloping search from index {}', 4 times, once per line.
#   and printed once 'Binary search from index 4 to 6' at last
def galloping_search(n, L):
    start = 0
    length_L = len(L)
    k = []
    while 2**start <= length_L:
        if L[2**start-1] < n:
            print('Galloping search from index {}'.format(2**start-1))
            start += 1
            k.append(start)
        else:
            print('Galloping search from index {}'.format(2**start-1))
            start += 1
            k.append(start)
            start += 1000
    if len(k) > 1:
        last = 2**(k[-1]-1)-1
        sec_last = 2 ** (k[-2]-1)-1
    else:
        last = 0
        sec_last = 0
        
    if binary_search(L, n):
        pos = L.index(n)
        if pos < last:
            print('Binary search from index {} to {}'.format(sec_last+1, last-1))
        elif pos == last:
            None
        elif pos < length_L-1:
            print('Binary search from index {} to {}'.format(last+1, pos+1))
        else:
            print('Galloping search from index {}'.format(length_L-1))
        return pos
    else:
        if L[last] > n:
            None
        elif L[-1] > n:
            print('Galloping search from index {}'.format(length_L-1))
        else:
            print('Galloping search from index {}'.format(length_L-1))
        return False
    
galloping_search(5, [1,2,3,4,5,6,7,8])    
    
# Test:
# Test1: n in the L
check.set_screen('Galloping search 0,1,3,7  Binary search 4 to 6')
check.expect('T1', galloping_search(5, [1,2,3,4,5,6,7,8]), 4)

check.set_screen('Galloping search 0')
check.expect('T2', galloping_search(1, [1,2,3,4,5,6,7,8,9]), 0)

check.set_screen('Galloping search 0,1,3,7  Binary search 4 to 6')
check.expect('T3', galloping_search(7, [1,2,3,4,5,6,7,8,9]), 6)

check.set_screen('Galloping search 0,1,3,7')
check.expect('T4', galloping_search(8, [1,2,3,4,5,6,7,8,9]), 7)

check.set_screen('Galloping search 0,1,3,7,8')
check.expect('T5', galloping_search(9, [1,2,3,4,5,6,7,8,9]), 8)

# Test2: n not in the L
check.set_screen('Galloping search 0,1,3,7')
check.expect('T6', galloping_search(12, [1,3,5,7,9,11,13,15,17]), False)

check.set_screen('Galloping search 0,1,3,7,8')
check.expect('T7', galloping_search(16, [1,3,5,7,9,11,13,15,17]), False)

check.set_screen('Galloping search 0,1,3')
check.expect('T8', galloping_search(6, [1,3,5,7,9,11,13,15,17]), False)

check.set_screen('Galloping search 0,1,3')
check.expect('T9', galloping_search(4, [1,3,5,7,9,11,13,15,17]), False)

check.set_screen('Galloping search 0,1,3,7,8')
check.expect('T10', galloping_search(18, [1,3,5,7,9,11,13,15,17]), False)

# Test3: Examples on Piazza
check.set_screen('Galloping search 0')
check.expect('T11', galloping_search(1, [2,3,4,5,6]), False)

check.set_screen('Galloping search 0,1')
check.expect('T12', galloping_search(3, [2,4,5,6,7]), False)

check.set_screen('Galloping search 0,1,2')
check.expect('T13', galloping_search(3, [1,2,4]), False)

check.set_screen('Galloping search 0,1,3,7,8')
check.expect('T14', galloping_search(8, [0,1,2,3,4,5,6,7,9]), False)

check.set_screen('Galloping search 0,1,3,4')
check.expect('T15', galloping_search(5, [0,1,2,3,4]), False)

check.set_screen('Galloping search 0,1,3,7,9, Binary search 8 to 8')
check.expect('T16', galloping_search(10, [1,2,3,4,5,6,7,8,9,100]), False)

check.set_screen('Galloping search 0,1,3,7, Binary search 8 to 13')
check.expect('T17', galloping_search(13, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), 12)

**** a07q4.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 07, Question 4
##===============================================
import math
import check
# Question 4 - part a
# helper_merge3(L1,L2) consumes two lists of natural numbers, L1 & L2, and
#   returns a new list contain L1 and L2 in ascending order
# helper_merge3: (listof Nat) (listof Nat) -> (listof Nat)
# Examples:
# helper_merge3([1,2],[5,8]) => [1,2,5,8]
def helper_merge3(L1,L2):
    L = L1 + L2
    i = 0
    j = 0
    index_L = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L[index_L] = L1[i]
            i += 1
        else:
            L[index_L] = L2[j]
            j += 1
        
        index_L += 1
    while i < len(L1):
        L[index_L] = L1[i]
        i += 1
        index_L += 1
    while j < len(L2):
        L[index_L] = L2[j]
        j += 1
        index_L += 1
    return L

# merge3(L1,L2,L3) consumes three lists of natural numbers, L1, L2 & L3, and 
#   returns a new list contain L1 L2 and L3 in ascending order
# merge3: (listof Nat) (listof Nat) (listof Nat) -> (listof Nat)
# Examples:
# merge3([1, 5], [2, 7], [3, 4, 9]) =>[1, 2, 3, 4, 5, 7, 9]

def merge3(L1, L2, L3):
    return helper_merge3(helper_merge3(L1,L2),L3)

# Test:
# Test1: Examples Test
check.expect('PartaT1', merge3([1,5], [2,7], [3,4,9]), [1,2,3,4,5,7,9])
# Test2: Non empty order 
check.expect('PartaT2', merge3([1,7],[4,5,6], [8,9,16]),[1,4,5,6,7,8,9,16])
check.expect('PartaT3', merge3([1,9],[2,2,2], [9,9,9]),[1,2,2,2,9,9,9,9])
check.expect('PartaT4', merge3([2,13],[2,12],[2,11]),[2,2,2,11,12,13])
check.expect('PartaT5', merge3([3,10], [2,9], [1, 6]), [1,2,3,6,9,10])
# Test3: empty order
check.expect('PartaT6', merge3([1,7],[4,5,6],[]),[1,4,5,6,7])
check.expect('PartaT7', merge3([], [],[1,2]),[1,2])
check.expect('PartaT8', merge3([],[], []),[])

# Question 4 - part b
# mergesort3(L): consumes a list of natural number, L, and returns a list of
#   natural number in ascending order
# mergesort3: (listof Nat) -> (listof Nat)
# Examples:
# mergesort3([2, 6, 1, 9, 3]) => [1, 2, 3, 6, 9]

def mergesort3(L):
    if len(L) > 1:
        first = math.ceil(len(L)/3)
        second = 2* first
        L1 = L[0:first]
        L2 = L[first: second]
        L3 = L[second:]
        L1 = mergesort3(L1)
        L2 = mergesort3(L2)
        L3 = mergesort3(L3)
        return merge3(L1,L2,L3)
    else:
        return L
# Test
# Test1: ascending order 
check.expect('PartbT1', mergesort3([1,2,3,4,5,6,7,8,9]), [1,2,3,4,5,6,7,8,9])
check.expect('PartbT2', mergesort3([1,3,5,7,9,11,13,15,17]), [1,3,5,7,9,11,13,15,17])
check.expect('PartbT3', mergesort3([2,4,6,8,10,22,30,31,40]), [2,4,6,8,10,22,30,31,40])
# Test2: decreasing order
check.expect('PartbT4', mergesort3([9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9])
check.expect('PartbT5', mergesort3([17,15,13,11,9,7,5,3,1]), [1,3,5,7,9,11,13,15,17])
check.expect('PartbT6', mergesort3([40,31,30,22,10,8,6,4,2]), [2,4,6,8,10,22,30,31,40])
# Test3: Chaos order
check.expect('PartbT7', mergesort3([2,4,1,8,3,0,5,2,3]), [0,1,2,2,3,3,4,5,8])
check.expect('PartbT8', mergesort3([2,3,1]), [1,2,3])
check.expect('PartbT9', mergesort3([88,33,99,11,44,22,0]), [0,11,22,33,44,88,99])
# Test4: Empty or len(L) < 3
check.expect('PartbT10', mergesort3([]), [])
check.expect('PartbT11', mergesort3([7,4]), [4,7])
check.expect('PartbT12', mergesort3([1]), [1])

**** End of graded assignment. *************************************************
