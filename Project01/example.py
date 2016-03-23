###########################################################################
# Example program for Computer Project #1
#
# Algorithm
#   prompt for two real numbers
#   display results of calculations
#   convert to integer numbers
#   display results of calculations
#   display results from selected functions from the math module
###########################################################################

import math

# Prompt the user for two real numbers

num1_str = input( "Please enter a real number: " )
num2_str = input( "Please enter another real number: " )

# Convert the user inputs into numeric values

num1_float = float( num1_str )
num2_float = float( num2_str )

# Display the values and selected calculations

print( )
print( "The real numbers are", num1_float, "and", num2_float )
print( "Addition:", num1_float + num2_float )
print( "Subtraction:", num1_float - num2_float )
print( "Multiplication:", num1_float * num2_float )
print( "Division:", num1_float / num2_float )

# Convert the real numbers to integer numbers

num1_int = int( num1_float )
num2_int = int( num2_float )

print( )
print( "The integer numbers are", num1_int, "and", num2_int )
print( "Addition:", num1_int + num2_int )
print( "Subtraction:", num1_int - num2_int )
print( "Multiplication:", num1_int * num2_int )
print( "Quotient:", num1_int // num2_int )
print( "Remainder:", num1_int % num2_int )

# Display the values returned by math functions

print( )
print( "The square root of", num1_float, "is", math.sqrt( num1_float ) )
print( "The ceiling of", num1_float, "is", math.ceil( num1_float ) )
print( "The floor of", num1_float, "is", math.floor( num1_float ) )

