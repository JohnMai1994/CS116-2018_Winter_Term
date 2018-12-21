##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 02, Question 4
##===============================================

import check
import math

# Question 4
## is_prime_num(a,b) returns True if a is the prime number, False if a is not the
##   prime number comsuming by a and b
## is_prime_num: Int Int => Bool
## requires: both a and b are positive integers
## Examples: 
## is_prime_num(5,2) => True
## is_prime_num(6,2) => False
def is_prime_num(a,b):
    if a == 1:
        return False
    elif a == b:
        return True
    elif a%b != 0:
        return is_prime_num(a, b+1)
    else:
        return False


## count_primes(start, end) return the number of prime numbers between start and
##    end(inclusive)
## count_primes: Int Int => Nat
## Requires:
## start and end are positive integers
## Examples:
## count_primes(1,10) => 4
## count_primes(5, 10) => 2
def count_primes(start,end):
    if start > end:
        return 0
    elif is_prime_num(start,2) == True:
        return 1 + count_primes(start+1, end)
    elif start == end:
        return 0    
    else:
        return count_primes(start+1,end)
    
## Test1: start from 1
check.expect("Q4Test1", count_primes(1, 11), 5)
check.expect("Q4Test2", count_primes(1, 15), 6)
## Test2: start from prime number
check.expect("Q4Test3", count_primes(3, 11), 4)
check.expect("Q4Test4", count_primes(5, 15), 4)
check.expect("Q4Test5", count_primes(3, 3), 1)
## Test3: start from non prime number
check.expect("Q4Test6", count_primes(4, 11), 3)
check.expect("Q4Test7", count_primes(6, 15), 3)
check.expect("Q4Test8", count_primes(4, 4), 0)
## Test4: start is larger than end
check.expect("Q4Test9", count_primes(11,3), 0)

        



    
