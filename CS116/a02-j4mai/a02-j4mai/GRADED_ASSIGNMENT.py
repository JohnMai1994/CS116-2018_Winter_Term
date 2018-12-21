ASSIGNMENT 02
Student's Quest ID: j4mai

**** Testing Results **********************************************************

53/53   Total Mark

 ** Question 1: 10/10
 ** Question 2: 8/8
 ** Question 3: 25/25
 ** Question 4: 10/10

(Question 1, Test t01, 1 marks): grade:All 0: Passed; passed.
(Question 1, Test t02, 1 marks): grade:Perfect: Passed; passed.
(Question 1, Test t03, 1 marks): grade:Failed Exams but > 45: Passed; passed.
(Question 1, Test t04, 1 marks): grade:Failed Exams but < 45: Passed; passed.
(Question 1, Test t05, 1 marks): grade:Passed Exams different: Passed; passed.
(Question 1, Test t06, 1 marks): grade:Failed Exams different: Passed; passed.
(Question 1, Test t07, 1 marks): grade:Failed everything but exams: Passed;
    passed.
(Question 1, Test t08, 1 marks): grade:Failed everything: Passed; passed.
(Question 1, Test t09, 1 marks): grade:80-90-88-0-0tut: Passed; passed.
(Question 1, Test t10, 1 marks): grade:50s-6tut: Passed; passed.
(Question 2, Test t01, 1 marks): feels:warm and dry; feels:cold and dry;
    feels:0 and dry: Passed; passed.
(Question 2, Test t02, 1 marks): feels:cool and breezy; feels:cold and breezy:
    Passed; passed.
(Question 2, Test t03, 1 marks): feels:cool and windy; feels:cold and windy:
    Passed; passed.
(Question 2, Test t04, 1 marks): feels:wc edge0; feels:wc edge1: Passed;
    passed.
(Question 2, Test t05, 1 marks): feels:normal; feels:hot: Passed; passed.
(Question 2, Test t06, 1 marks): feels:humid; feels:hot and humid: Passed;
    passed.
(Question 2, Test t07, 1 marks): feels:hdx edge0; feels:hdx edge1: Passed;
    passed.
(Question 2, Test t08, 1 marks): feels:T edge hum; feels:T edge wc: Passed;
    passed.
(Question 3, Test t01, 1 marks): forecast:low:steady: Passed; passed.
(Question 3, Test t02, 1 marks): forecast:mod:steady: Passed; passed.
(Question 3, Test t03, 1 marks): forecast:hi:steady: Passed; passed.
(Question 3, Test t04, 1 marks): forecast:low:+: Passed; passed.
(Question 3, Test t05, 1 marks): forecast:mod:+: Passed; passed.
(Question 3, Test t06, 1 marks): forecast:hi:+: Passed; passed.
(Question 3, Test t07, 1 marks): forecast:low:++: Passed; passed.
(Question 3, Test t08, 1 marks): forecast:mod:++: Passed; passed.
(Question 3, Test t09, 1 marks): forecast:hi:++: Passed; passed.
(Question 3, Test t10, 1 marks): forecast:low:-: Passed; passed.
(Question 3, Test t11, 1 marks): forecast:mod:-: Passed; passed.
(Question 3, Test t12, 1 marks): forecast:hi:-: Passed; passed.
(Question 3, Test t13, 1 marks): forecast:low:^a: Passed; passed.
(Question 3, Test t14, 1 marks): forecast:mod:^a: Passed; passed.
(Question 3, Test t15, 1 marks): forecast:hi:^a: Passed; passed.
(Question 3, Test t16, 1 marks): forecast:low_edge:+: Passed; passed.
(Question 3, Test t17, 1 marks): forecast:mod_edge_l:+: Passed; passed.
(Question 3, Test t18, 1 marks): forecast:mod_edge_u:+: Passed; passed.
(Question 3, Test t19, 1 marks): forecast:hi_edge:+: Passed; passed.
(Question 3, Test t20, 1 marks): forecast:mod_edge:++: Passed; passed.
(Question 3, Test t21, 1 marks): forecast:hi_edge:++: Passed; passed.
(Question 3, Test t22, 1 marks): forecast:low_edge:^a: Passed; passed.
(Question 3, Test t23, 1 marks): forecast:mod_edge:^a: Passed; passed.
(Question 3, Test t24, 1 marks): forecast:mod_edge:-: Passed; passed.
(Question 3, Test t25, 1 marks): forecast:hi_edge:-: Passed; passed.
(Question 4, Test t01, 1 marks): primes:empty: Passed; passed.
(Question 4, Test t02, 1 marks): primes:none: Passed; passed.
(Question 4, Test t03, 1 marks): primes:not-one: Passed; passed.
(Question 4, Test t04, 1 marks): primes:not-one: Passed; passed.
(Question 4, Test t05, 1 marks): primes:one value: Passed; passed.
(Question 4, Test t06, 1 marks): primes:one value wider: Passed; passed.
(Question 4, Test t07, 1 marks): primes:two values narrow: Passed; passed.
(Question 4, Test t08, 1 marks): primes:two: Passed; passed.
(Question 4, Test t09, 1 marks): primes:more:: Passed; passed.
(Question 4, Test t10, 1 marks): primes:mid: Passed; passed.
5 control characters removed.


**** testing_result.txt *****************************************************************
Total number of tests missing: 4

earned_grade: All 5 required cases were tested.

feels_like: All 4 required cases were tested.

weather_forecast: 3 of the 15 required cases were missing:
 - Moderate Pressure -
 - Edge Case for Low/Moderate Pressure
 - Edge Case for High/Moderate Pressure

count_primes: 1 of the 5 required cases were missing:
 - Special: No primes



**** a02q1.py *****************************************************************
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


**** a02q2.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 02, Question 2
##===============================================

import check
import math

# Question 2
## feels_like(temp, wind, hum) return the currently "fells like" for human being
##   by consuming current temperature(temp), wind speed(wind) and relative 
##   humidity percentage(hum)

## feels_like: Float, Float, Nat => Float

## Requires:
## wind is a non-negative value
## hum between 0 and 100 (inclusive)

## Examples
## feels_like(-9.5,1.9,91) => -9.5

def feels_like(temp, wind, hum):
  windchill = 13.12 + 0.6125*temp - 11.37*wind**0.16 + 0.3965*temp*wind**0.16
  vapour_pressure = 6.112* 10**(7.5*temp/(237.7+temp)) *(hum/100)
  humidex = temp + 5/9*(vapour_pressure -10)
  if temp >= 15:
    if humidex - temp >= 1:
      return humidex
    else:
      return temp
  else:
    if temp - windchill >= 1:
      return windchill
    else:
      return temp

## Test1: temp higher than 15, humidex minus temp higher than 1
check.within("Q2Test1", feels_like(16, 2, 99), 20.43398, 0.0001)
## Test2: temp higher than 15, humidex minus temp less than 1
check.within("Q2Test2", feels_like(16, 2, 50), 16, 0.0001)
## Test3: temp lower than 15, windchill minus temp higher than 1
check.within("Q2Test3", feels_like(-1, 4, 30), -2.18098, 0.0001)
## Test4: temp lower than 15, windchill minus temp less than 1
check.within("Q2Test4", feels_like(-1, 2, 50), -1, 0.0001)
check.within("Q2Test5", feels_like(-9.5,1.9,91), -9.5, 0.0001)

**** a02q3.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 02, Question 3
##===============================================

import check
import math

# Question 3

## Useful constants for pressure trends
steady = "Steady"
rising_s = "Rising Slowly"
rising_f = "Rising Quickly"
falling_s = "Falling Slowly"
falling_f = "Falling Quickly"

## Useful constants for forecasts
no_change = "No Change"
sun = "Sunny"
storm = "Storms"
tornado = "Tornado Watch"
wind = "Windy"
rain = "Rain"
cloud = "Cloudy"

## weather_forecast(pressure, trend) returns the weather forecast according to 
##   the different pressure and trend combination in the weather prediction table

## weather_forecast: Float, Str => Str

## Requires:
## pressure between 80.0kPa and 120.0kPa

## Examples
## weather_forecast(101.7, "Falling Slowly") => "Rain"

def weather_forecast(pressure,trend):
  if trend == steady:
    return no_change
  elif trend == rising_s:
    if pressure < 100:
      return no_change
    elif pressure <= 103:
      return sun
    else:
      return sun
  elif trend == rising_f:
    if pressure < 100:
      return sun
    elif pressure <= 103:
      return wind
    else:
      return sun
  elif trend == falling_s:
    if pressure < 100:
      return storm
    elif pressure <= 103:
      return rain
    else: 
      return no_change
  else:
    if pressure < 100:
      return tornado
    elif pressure <= 103:
      return storm
    else:
      return cloud
  
## Test1: weather is no change
check.expect("Q3Test1", weather_forecast(102, steady), "No Change")
check.expect("Q3Test2", weather_forecast(99, "Rising Slowly"), "No Change")
check.expect("Q3Test3", weather_forecast(110, "Falling Slowly"), "No Change")
## Test2: weather is sunny
check.expect("Q3Test4", weather_forecast(98.7, "Rising Quickly"), "Sunny")
check.expect("Q3Test5", weather_forecast(102,"Rising Slowly"), "Sunny")
check.expect("Q3Test6", weather_forecast(111.2, "Rising Slowly"), "Sunny")
check.expect("Q3Test7", weather_forecast(111, "Rising Quickly"), "Sunny")
## Test3: weather is storms
check.expect("Q3Test8", weather_forecast(99.5, "Falling Slowly"), "Storms")
check.expect("Q3Test9", weather_forecast(101, "Falling Quickly"), "Storms")
## Test4: weather is Tornado Watch
check.expect("Q3Test10", weather_forecast(99.3, "Falling Quickly"), "Tornado Watch")
## Test5: weather is windy
check.expect("Q3Test11", weather_forecast(102.1, "Rising Quickly"), "Windy")
## Test6: weather is cloudy
check.expect("Q3Test12", weather_forecast(116.8, "Falling Quickly"), "Cloudy")

**** a02q4.py *****************************************************************
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

        



    


**** End of graded assignment. *************************************************
