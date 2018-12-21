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
