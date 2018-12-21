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
