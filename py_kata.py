""" Module for codewars kata practice """

# 01/01/2024
# Grade book
# Complete the function so that it finds the average of the three scores passed
#  to it and returns the letter value associated with that grade.
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for
# negative values or values greater than 100.

# def get_grade(s1, s2, s3):
#     sav = (s1+s2+s3)/3
#     if 90 <= sav <= 100:
#         return "A"
#     elif 80 <= sav <= 90:
#         return "B"
#     elif 70 <= sav <= 80:
#         return "C"
#     elif 60 <= sav <= 70:
#         return "D"
#     else:
#         return "F"

# print(get_grade(95, 90, 93)) # A

# # 02/01/2024
# # Write a function that accepts an integer n and a string s as parameters,
#  and returns a string of s repeated exactly n times.
# # Examples (input -> output)
# # 6, "I"     -> "IIIIII"
# # 5, "Hello" -> "HelloHelloHelloHelloHello"

# def repeat_str(repeat, string):
#     return string * repeat

# print(repeat_str(6, "I")) # IIIIII

# # 03/01/2024
# # It's pretty straightforward. Your goal is to create a function that removes
#  the first and last characters of a string. You're given one parameter, the
#  original string. You don't have to worry with strings with less than two
#  characters.

# def remove_char_a(a):
#     return a[1:-1]
# print(remove_char_a("eloquent")) # loquen

# 04/01/2024
# You will be given an array a and a value x. All you need to do is check
#  whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

# def check(seq, elem):
#     return elem in seq
#     # return True if elem in seq else False

# a = [2, 4, 6, 8]
# x = 2

# print(check(a, x))

# 05/01/2024
# Implement a function which convert the given boolean value into its string
#  representation.
# Note: Only valid inputs will be given.

# def boolean_to_string(b):
#     return str(b)

# b = True
# print(boolean_to_string(b))

# DESCRIPTION:
# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.
# About factors
# Factors are numbers you can multiply together to get another number.
# 2 and 3 are factors of 6 because: 2 * 3 = 6
# You can find a factor by dividing numbers. If the remainder is 0 then the
#  number is a factor.
# You can use the mod operator (%) in most languages to check for a remainder
# For example 2 is not a factor of 7 because: 7 % 2 = 1
# Note: base is a non-negative number, factor is a positive number.

# """function to test if the factor is a factor of base """
# def check_for_factor(base, factor):
#     return base%factor == 0

# print(check_for_factor(6,2))
# # print(7%2)

# 06/01/2024

# The Story:
# Bob is working as a bus driver. However, he has become extremely popular
#  amongst the city's residents. With so many passengers wanting to get
#  aboard his bus, he sometimes has to face the problem of not enough space
#  left on the bus! He wants you to write a simple program telling him if he
#  will be able to fit all the passengers.
# Task Overview:
# You have to write a function that accepts three parameters:
# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the
#  driver.
# If there is enough space, return 0, and if there isn't, return the number of
#  passengers he can't take.
# Usage Examples:
# cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
# cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting

# Function to check if there is enough space on the bus
# def enough(cap, on, wait):
#     return '0' if (on + wait) <= cap else (on + wait - cap)

# result = enough(10, 5, 5)
# print(result)

# 07/01/2024
# Copilot kata:
# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.

def other_angle(a, b):
    return 180 - a - b

print(other_angle(30, 60))

# codewars kata:
# Very simple, given an integer or a floating-point number, find its opposite.
# Examples:
# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    return -number

print(opposite(3))
