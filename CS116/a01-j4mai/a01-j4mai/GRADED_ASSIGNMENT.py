ASSIGNMENT 01
Student's Quest ID: j4mai

**** Testing Results **********************************************************

50/50   Total Mark

 ** Question 1: 9/9
 ** Question 2: 8/8
 ** Question 3: 24/24
 ** Question 4: 9/9

(Question 1, Test t01, 1 marks): ^aIphone^a: Passed; passed.
(Question 1, Test t02, 1 marks): LG G5: Passed; passed.
(Question 1, Test t03, 1 marks): Blackberry Priv, Waterloo to Laurier campus:
    Passed; passed.
(Question 1, Test t04, 1 marks): phone length < distance: Passed; passed.
(Question 1, Test t05, 1 marks): phone length = distance: Passed; passed.
(Question 1, Test t06, 1 marks): distance is multiple of phone_length: Passed;
    passed.
(Question 1, Test t07, 1 marks): distance is slightly more than a multiple of
    phone_length: Passed; passed.
(Question 1, Test t08, 1 marks): distance is just less than a multiple of
    phone_length: Passed; passed.
(Question 1, Test t09, 1 marks): distance is 2.5 times length, answer is 3:
    Passed; passed.
(Question 2, Test t01, 1 marks): fib(0): Passed; passed.
(Question 2, Test t02, 1 marks): fib(1): Passed; passed.
(Question 2, Test t03, 1 marks): fib(2): Passed; passed.
(Question 2, Test t04, 1 marks): fib(3): Passed; passed.
(Question 2, Test t05, 1 marks): fib(5): Passed; passed.
(Question 2, Test t06, 1 marks): fib(10): Passed; passed.
(Question 2, Test t07, 1 marks): fib(20): Passed; passed.
(Question 2, Test t08, 1 marks): fib(50): Passed; passed.
(Question 3, Test t01, 1 marks): ^agrade: All 0^a: Passed; passed.
(Question 3, Test t02, 1 marks): ^agrade: Perfect^a: Passed; passed.
(Question 3, Test t03, 1 marks): ^agrade: Regular marks^a: Passed; passed.
(Question 3, Test t04, 1 marks): ^agrade: Regular marks with 0 tutorials^a:
    Passed; passed.
(Question 3, Test t05, 1 marks): ^agrade: Regular marks with few tutorial^a:
    Passed; passed.
(Question 3, Test t06, 1 marks): ^agrade: Regular marks with all tutorial:
    Passed; passed.
(Question 3, Test t07, 1 marks): grade: All are 50% with no tutorial: Passed;
    passed.
(Question 3, Test t08, 1 marks): grade: All are 50% with 6 tutorial: Passed;
    passed.
(Question 3, Test t09, 1 marks): grade: All are 50% with all tutorials:
    Passed; passed.
(Question 3, Test t10, 1 marks): grade: Failed exams with low assignment and
    no tutorials: Passed; passed.
(Question 3, Test t11, 1 marks): grade: Failed exams with low assignment and 6
    tutorials: Passed; passed.
(Question 3, Test t12, 1 marks): grade: No Assignment marks, clickers, and tu-
    torials: Passed; passed.
(Question 3, Test t13, 1 marks): grade: Midterm failed and no tutorials:
    Passed; passed.
(Question 3, Test t14, 1 marks): Failing grade: low scores overall with few
    tutorials: Passed; passed.
(Question 3, Test t15, 1 marks): Failing grade: low exam scores: Passed;
    passed.
(Question 3, Test t16, 1 marks): Failing grade: low scores overall, no tutori-
    als: Passed; passed.
(Question 3, Test t17, 1 marks): High Assignment and exams, perfect clicker
    and tutorial: Passed; passed.
(Question 3, Test t18, 1 marks): High Assignment and exams: perfect clicker
    but no tutorial: Passed; passed.
(Question 3, Test t19, 1 marks): High Assignment and exams: No clicker and tu-
    torial: Passed; passed.
(Question 3, Test t20, 1 marks): High Assignment and exams: No clicker with
    most tutorial: Passed; passed.
(Question 3, Test t21, 1 marks): High Assignment and exams: Partial Clicker,
    with no tutorial: Passed; passed.
(Question 3, Test t22, 1 marks): High Assignment and exams: partial clicker
    and few tutorial: Passed; passed.
(Question 3, Test t23, 1 marks): High Assignment and exams: partial clicker
    and most tutorial: Passed; passed.
(Question 3, Test t24, 1 marks): High Assignment and exams: partial clicker
    and all tutorial: Passed; passed.
(Question 4, Test t01, 1 marks): ^asecret: given example^a: Passed; passed.
(Question 4, Test t02, 1 marks): ^asecret: min secret value^a: Passed; passed.
(Question 4, Test t03, 1 marks): ^asecret: larger-one-digit^a: Passed; passed.
(Question 4, Test t04, 1 marks): ^asecret: two-digit^a: Passed; passed.
(Question 4, Test t05, 1 marks): ^asecret: larger secret^a: Passed; passed.
(Question 4, Test t06, 1 marks): ^asecret: fav_month=fav_day=1: Passed; passed\
.
(Question 4, Test t07, 1 marks): secret: fav_month=1,fav_day=31: Passed;
    passed.
(Question 4, Test t08, 1 marks): secret: fav_month=12,fav_day=1: Passed;
    passed.
(Question 4, Test t09, 1 marks): secret: fav_month=12,fav_day=31: Passed;
    passed.
24 control characters removed.


**** testing_result.txt *****************************************************************
Total number of tests missing: 1

how_many_phones: 1 of the 5 required cases were missing:
 - Small Phone

fibonacci: All 3 required cases were tested.

basic_grade: All 5 required cases were tested.

reveal_secret: All 3 required cases were tested.



**** a01q1.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 01, Question 1
##===============================================

import math
import check

## QUESTION 1
## how_many_phone(phone_length, distance) return the minimum natural number 
##  of cell phones that are needed to be placed end-to-end to cover distance km
##  with phone_length cm

## how_many_phones: (anyof Int Float) (anyof Int Float) -> Nat

## Examples
## how_many_phones (14.7, 1.6) => 10885
## how_many_phones (10, 1) => 10000

def how_many_phones(phone_length, distance):
    km = 1000
    m = 100
    val = math.ceil (distance*km*m/phone_length)
    return val

## Test 1: Regular Situation
check.expect("Q1Test1",how_many_phones(14.7,1.6),10885)
check.expect("Q1Test2",how_many_phones(20,1),5000)

## Test 2: distance less than phone_length
check.expect("Q1Test3",how_many_phones(1000, 0.0005), 1)

**** a01q2.py *****************************************************************
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


**** a01q3.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 01, Question 3
##===============================================

import math
import check

## QUESTION 3
## basic_grade(assts, mid_exam, final_exam, clickers, tutorials) return the basic
##   grade based on the grading scheme, 20% Assts, 30% mid_exam, 45% final_exam
##   5% for clickers and tutorials times

## basic_grade: Float Float Float Float Nat -> Nat

## Require:
##   assts, mid_exam, final_exam and clickers are floating point value between
##   0 and 100 (inclusive)
##   tutorials is natural number between 1 and 12 (inclusive)

## Examples
## basic_grade(60.0, 75.8, 90.0, 55.5, 9) => 79
## baisc_grade(0.0, 0.0, 0.0, 0.0, 10) => 1

def basic_grade(assts, mid_exam, final_exam, clickers, tutorials):
    ea_part = (0.2 * assts) + (0.3 * mid_exam) +(0.45 * final_exam)
    participation = min(5, 0.05 * clickers + 0.1 * tutorials)
    return round (ea_part + participation)

## Test1: Regular Situation
check.expect("q3Test1", basic_grade(60.0, 75.8, 90.0, 55.5, 9), 79)

## Test2: No assignment, midterm and final grade
check.expect("q3Test2", basic_grade(0.0, 0.0, 0.0, 0.0, 10), 1)

## Test3: Participation Grade is not maximum
check.expect("q3Test3", basic_grade(80, 90, 78, 50, 2), 81)

## Test4: Full mark
check.expect("q3Test4", basic_grade(100, 100, 100, 100, 12), 100)

**** a01q4.py *****************************************************************
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

**** End of graded assignment. *************************************************
