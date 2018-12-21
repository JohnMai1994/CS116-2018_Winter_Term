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
