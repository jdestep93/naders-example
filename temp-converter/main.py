from pip._vendor.distlib.compat import raw_input

# The goal of this program is to convert celsius to fahrenheit and vice versa based on user info provided

# Want to acquire if the user is converting from Celsius to Fahrenheit or F to C (store in variable called option)
print('Do you want to convert from Fahrenheit to Celsius, or Celsius to Fahrenheit? Enter 1 for Fahrenheit to Celsius, Enter 2 for Celsius to Fahrenheit')
# you would use int(raw_input()) for a whole number, float() is to capture the raw input as a number with a decimal value
option = float(raw_input())

# make sure the option entered is 1 or 2, otherwise raise an Exception (an error in programming)
if option != 1 and option != 2:
    raise Exception('Sorry, you must enter 1 or 2 as the option to convert temperature!')

# stores the original temperature's unit of measure
originalTempUnit = 'Fahrenheit'

if option == 2:
    originalTempUnit = 'Celsius'

# Prompt the user of the program to enter the temperature
print('Please enter the temperature in ' + originalTempUnit)
temperature = float(raw_input())

# Based on user inputted Celsius or Fahrenheit, calculate the number in the opposite unit as expected
# (32°F − 32) × 5/9 = 0°C - this is F to C
# (0°C × 9/5) + 32 = 32°F
# these variables store the final temperature and the Unit (F or C) of the final temperature calculation
finalTempUnit = 'Fahrenheit'
finalTemperature = 0

# if option is equal to 1 (F to C), convert from Fahrenheit to Celsius and store in the final temperature variable
if option == 1:
    finalTemperature = (temperature - 32) * (5 / 9)
    # set the final string for display as displaying Celsius
    finalTempUnit = 'Celsius'
# if option is equal to 2 (C to F), convert from Celsius to Fahrenheit and store in the final temperature variable
elif option == 2:
    finalTemperature = (temperature * (9 / 5)) + 32

# Output the results to the user
# constructs a string for the final output to display for the user
print('Original temperature in ' + originalTempUnit + ': ' + str(temperature) + ', ' + finalTempUnit + ': ' + str(finalTemperature))
