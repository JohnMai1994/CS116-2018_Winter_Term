##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 01, Question 2
##===============================================

import math
import check

## QUESTION 2
## fibonacci(n) return an integer which is the nth Fibonacci number

## fibonacci: Nat -> Int

## Examples:
## fibonacci(1) => 1
## fibonacci(6) => 8

def fibonacci(n): 
    k = (1 + math.sqrt (5))/2
    f = (k**n - ((-1)/k)**n)/ math.sqrt(5)
    return math.floor(f)

## Test1: n >= 1
check.expect("Q2Test1",fibonacci(6), 8)
check.expect("Q2Test2",fibonacci(8), 21)
check.expect("Q2Test3",fibonacci(10), 55)
check.expect("Q2Test4",fibonacci(11), 89)

## Test2: n = 0
check.expect("Q2test5",fibonacci(0), 0)
