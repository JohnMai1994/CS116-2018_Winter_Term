##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 06, Question 2
##===============================================
import check
# Question 2
# find_bigger(ints) consumes a (listof Int), ints, and returns a (listof Int)
#   which values in the list that are bigger than all values that came before 
#   in the list
# find_bigger: (listof Int) -> (listof Int)
# Examples:
# find_bigger([0, 4, 5, 4]) => [0, 4, 5]
# find_bigger([1, 2, 4, 4]) => [1, 2, 4]
# find_bigger([-2, -4, -4, -1]) => [-2, -1]
# find_bigger([]) => []

def find_bigger(ints):
    if ints==[]:
        return []
    else:
        num = -1
        z = [ints[0]]
        max_num = ints[0]
        for k in ints:
            if max_num < k:
                max_num = max(max_num, k)
                z.append(k)
                num +=1
            else:
                num +=1
        return z

# Test:
# Test1: empty list
check.expect('empty', find_bigger([]), [])
# Test2: increasing order
check.expect('Increase Order1', find_bigger([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
check.expect('Increase Order2', find_bigger([1,3,3,4,6,6,8]), [1,3,4,6,8])
check.expect('Increase Order3', find_bigger([1,2,4,5,8,10]), [1,2,4,5,8,10])
check.expect('Increase Order4', find_bigger([1,5,8,12,33,99]), [1,5,8,12,33,99])
check.expect('Increase Order5', find_bigger([1,15,15,15,90]), [1,15,90])
check.expect('Increase Order6', find_bigger([1,5,6,7]), [1,5,6,7])
# Test3: decreasing order
check.expect('Decreasing Order1', find_bigger([9,8,7,6,5,4,3]), [9])
check.expect('Decreasing Order2', find_bigger([19,7,4,2]), [19])
check.expect('Decreasing Order3', find_bigger([99,55,32,32,12,0]), [99])
check.expect('Decreasing Order4', find_bigger([87,4,3,67,3]), [87])
check.expect('Decreasing Order5', find_bigger([9,8,8,8,8,8,8]), [9])
check.expect('Decreasing Order6', find_bigger([9,8,2,9,4]), [9])
# Test4: up-down-up order
check.expect('Up-Down-UP Order1', find_bigger([2,6,9,8,7,7,5,8,10]), [2,6,9,10])
check.expect('Up-Down-UP Order2', find_bigger([2,19,7,5,100,101]), [2,19,100,101])
check.expect('Up-Down-UP Order3', find_bigger([2,20,21,20,21,22]), [2,20,21,22])
# Test5: All Same
check.expect('All Same', find_bigger([2,2,2,2,2]), [2])
check.expect('All Same', find_bigger([5,5,5]), [5])
# Test6: Sample Question
check.expect('Sample Question1', find_bigger([0, 4, 5, 4]), [0,4,5])
check.expect('Sample Question2', find_bigger([1,2,4,4]), [1,2,4])
check.expect('Sample Question3', find_bigger([-2,-4,-4,-1]), [-2,-1])

