##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 02, Question 1
##===============================================

import check
import math

# Question 1
## earned_grade(assts, mid_exam, final_exam, clickers, tutorials) returns the 
##   basic grade based on the grading scheme, 20% Assts, 30% mid_exam, 45% final_exam
##   5% for clickers and tutorials times.

## earned_grade: Float, Float, Float, Float, Int => Int

## Require:
##   assts, mid_exam, final_exam and clickers are floating point value between
##   0 and 100 (inclusive)
##   tutorials is natural number between 1 and 12 (inclusive)

## Examples:
## earned_grade(60.0, 55.8, 40.0, 55.5, 9) => 45
## earned_grade(10.0, 5.0, 40.0, 12.0, 0) => 22

def earned_grade(assts, mid_exam, final_exam, clickers, tutorials):
  assts_rate = 0.2
  mid_rate = 0.3
  final_rate = 0.45
  part_rate = 0.05
  exam_average = (mid_rate * mid_exam + final_rate * final_exam) /75
  grade = (assts_rate * assts) + (mid_rate * mid_exam) +\
    (final_rate * final_exam) + min(5, (part_rate*clickers) + 0.1*tutorials)  
  if exam_average >= 0.5:
    return round(grade)
  else:
    return round(min(45, grade))

## Test1: exam average less than 50%, the grade is higher than 45
check.expect("Q1Test1", earned_grade(60.0,55.8,40.0,55.5,9), 45)
## Test2: exam average less than 50%, the grade is less than 45
check.expect("Q1Test2", earned_grade(10.0, 5.0, 40.0, 12.0, 0), 22)
## Test3: exam average higher than 50%, the grade is less than 45
check.expect("Q1Test3", earned_grade(0, 51, 51, 0, 0), 38)
## Test4: exam average higher than 50%, the grade is higher than 45
check.expect("Q1Test4", earned_grade(100, 100, 100, 100, 12), 100)
