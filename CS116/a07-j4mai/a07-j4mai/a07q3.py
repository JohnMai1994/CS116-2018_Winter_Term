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
