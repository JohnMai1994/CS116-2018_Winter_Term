##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 03, Question 2
##===============================================

import check

# Q2
# bin2nat(bistr) returns a natural number representing the decimal value of 
#    bistr
# bin2nat: Str -> Nat
# Requires:
# Bistr is a non-empty string only contain "0" and "1"
# Examples:
# bin2nat("101") => 5
# bin2nat("1111") => 15

def bin2nat(bistr):
    mul_times = len(bistr) -1
    if mul_times == -1:
        return 0
    else:
        num = int(bistr[0:1])
    return num*(2**mul_times) + bin2nat(bistr[1:])

# Test1: all 0
check.expect("Q2Test1", bin2nat("000000"), 0)
# Test2: all 1
check.expect("Q2Test2", bin2nat("1"), 1)
check.expect("Q2Test3", bin2nat("11"), 3)
check.expect("Q2Test4", bin2nat("111"), 7)
check.expect("Q2Test5", bin2nat("1111"), 15)
# Test3: contain 1 and 0
check.expect("Q2Test6", bin2nat("101"), 5)
check.expect("Q2Test7", bin2nat("1011"), 11)
check.expect("Q2Test8", bin2nat("1010101"), 85)
