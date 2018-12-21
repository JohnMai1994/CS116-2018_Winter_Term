##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 01, Question 4
##===============================================

import math
import check

## QUESTION 4

## reveal_secret(secret, fav_month, fav_day) returns the value of secret by 
##   consuming secret, fav_month and fav_day

## reveal_secret: Int Int Int -> Int

## Require
##   secret > 2
##   fav_month between 1 and 12 (inclusive)
##   fav_day between 1 and 31 (inclusive)

## Examples
## reveal_secret(101, 9, 12) => 101
## reveal_secret(6, 10, 31) => 6

def reveal_secret(secret, fav_month, fav_day):
    a = secret * 3
    b = a + secret - 5
    c = b * 3 * 3
    d = c + secret - fav_month
    e = d * 3 * 3 * 3
    f = e + secret - fav_day
    g = (f // 1000) + 2
    return g

## Test1: Secret number units digit, tens and hundreds
check.expect("Q4Test1", reveal_secret(6, 5, 11), 6)
check.expect("Q4Test2", reveal_secret(88, 9, 10), 88)
check.expect("Q4Test3", reveal_secret(885, 10, 25), 885)

## Test2: choise Dec.31 as the fav_month and fav_day
check.expect("Q4Test4", reveal_secret(3, 12, 31), 3)

## Test3: choise Jan.1 as the fav_month and fav_day
check.expect("Q4Test4", reveal_secret(3, 1, 1), 3)
