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
