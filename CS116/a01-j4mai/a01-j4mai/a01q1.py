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
