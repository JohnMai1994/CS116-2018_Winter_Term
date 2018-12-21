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
