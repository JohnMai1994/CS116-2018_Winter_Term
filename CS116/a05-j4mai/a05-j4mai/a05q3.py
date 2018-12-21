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
