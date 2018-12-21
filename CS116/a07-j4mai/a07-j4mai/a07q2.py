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
