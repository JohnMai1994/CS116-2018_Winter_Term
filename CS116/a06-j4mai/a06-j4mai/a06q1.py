##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 06, Question 1
##===============================================
## In each function, copy the function header to your own file. 
## Your solution will replace "pass" in the body of the functions.
import check
# Question 1 - part a
# nat2bin(n) return a non-empty list which is the binary digits by consuming 
#   a Nat number, n.
# nat2bin: Nat -> (listof (anyof 0 1))
# require:
# n >= 0
# Examples:
# nat2bin(12) => [1, 1, 0, 0]
# nat2bin(5) => [1, 0, 1]
# nat2bin(2) => [1, 0]
# nat2bin(0) => [0]

def nat2bin(n):
    if n == 0:
        return [0]
    else:
        list_num = 0
        while n >= 2**list_num:
            list_num += 1
            alist = list(range(list_num))
            alist.reverse()
            value_list = []
        for i in alist:
            append = n // 2**i
            n = n % 2**i
            value_list.append(append)
        return value_list
# Test:
# Test1: 0 - 9
check.expect('n=0', nat2bin(0), [0])
check.expect('n=1', nat2bin(1), [1])
check.expect('n=2', nat2bin(2), [1,0])
check.expect('n=3', nat2bin(3), [1,1])
check.expect('n=4', nat2bin(4), [1,0,0])
check.expect('n=6', nat2bin(6), [1,1,0])
check.expect('n=5', nat2bin(5), [1,0,1])
check.expect('n=8', nat2bin(8), [1,0,0,0])
check.expect('n=9', nat2bin(9), [1,0,0,1])
# Test2: 10 - 99
check.expect('n=12', nat2bin(12), [1,1,0,0])
check.expect('n=25', nat2bin(25), [1,1,0,0,1])
check.expect('n=38', nat2bin(38), [1,0,0,1,1,0])
check.expect('n=49', nat2bin(49), [1,1,0,0,0,1])
check.expect('n=58', nat2bin(58), [1,1,1,0,1,0])
check.expect('n=79', nat2bin(79), [1,0,0,1,1,1,1])
# Test3: bigger than 100
check.expect('n=100', nat2bin(100), [1,1,0,0,1,0,0])
check.expect('n=250', nat2bin(250), [1,1,1,1,1,0,1,0])
        
# Question 1 - part b
# nat2base(n, base) consumes two Nat,n and base, and returns a list of Nat 
# representing n in the base given by base.
# nat2base: Nat Nat -> (listof Nat)
# requires:
# n >= 0, base >= 0
# examples:
# nat2base(12, 2) => [1, 1, 0, 0]
# nat2base(245, 10) => [2, 4, 5]
# nat2base(326, 5) => [2, 3, 0, 1]
# nat2base(165, 16) => [10, 5]
# nat2base(36, 36) => [1, 0]

def nat2base(n, base):
    if n == 0:
        return [0]
    else:
        list_num = 0
        while n >= base**list_num:
            list_num += 1
            alist = list(range(list_num))
            alist.reverse()
            value_list = []
        for i in alist:
            append = n // base**i
            n = n % base**i
            value_list.append(append)
        return value_list        

# Test:
# Test1: n from 0 to 150, base = 2
check.expect('n=0, base=2', nat2base(0,2), [0])
check.expect('n=5, base=2', nat2base(5,2), [1,0,1])
check.expect('n=17, base=2', nat2base(17,2), [1,0,0,0,1])
check.expect('n=24, base=2', nat2base(24,2), [1,1,0,0,0])
check.expect('n=63, base=2', nat2base(63,2), [1,1,1,1,1,1])
check.expect('n=97, base=2', nat2base(97,2), [1,1,0,0,0,0,1])
check.expect('n=149, base=2', nat2base(149,2), [1,0,0,1,0,1,0,1])
# Test2: n from 0 to 150, base =5
check.expect('n=0, base=5', nat2base(0,5), [0])
check.expect('n=5, base=5', nat2base(5,5), [1,0])
check.expect('n=15, base=5', nat2base(15,5), [3,0])
check.expect('n=25, base=5', nat2base(25,5), [1,0,0])
check.expect('n=78, base=5', nat2base(78,5), [3,0,3])
check.expect('n=49, base=5', nat2base(49,5), [1,4,4])
check.expect('n=50, base=5', nat2base(50,5), [2,0,0])
check.expect('n=150, base=5', nat2base(150,5), [1,1,0,0])
# Test3: n from 0 to 150, base = 17
check.expect('n=0, base=17', nat2base(0,17), [0])
check.expect('n=17, base=17', nat2base(17,17), [1,0])
check.expect('n=34, base=17', nat2base(34,17), [2,0])
check.expect('n=56, base=17', nat2base(56,17), [3,5])
check.expect('n=77, base=17', nat2base(77,17), [4,9])
check.expect('n=99, base=17', nat2base(99,17), [5,14])
check.expect('n=132, base=17', nat2base(132,17), [7,13])
# Test4: n from 0 to 500, base = 36
check.expect('n=0, base=36', nat2base(0,36), [0])
check.expect('n=36, base=36', nat2base(36,36), [1,0])
check.expect('n=72, base=36', nat2base(72,36), [2,0])
check.expect('n=90, base=36', nat2base(90,36), [2,18])
check.expect('n=150, base=36', nat2base(150,36), [4,6])
check.expect('n=260, base=36', nat2base(260,36), [7,8])
check.expect('n=360, base=36', nat2base(360,36), [10,0])


