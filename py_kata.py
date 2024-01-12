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

# def other_angle(a, b):
#     return 180 - a - b

# print(other_angle(30, 60))

# codewars kata:
# Very simple, given an integer or a floating-point number, find its opposite.
# Examples:
# 1: -1
# 14: -14
# -34: 34

# def opposite(number):
#     return -number

# print(opposite(3))

# 08/02/2024
# 7 kyu - Sum of odd numbers
# Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
# 1 -->  1
# 2 --> 3 + 5 = 8
# 3 --> 7 + 9 + 11 = 27

# def row_sum_odd_numbers(n):
#     return n**3

# print(row_sum_odd_numbers(3))

# # 09/02/2024
# # 7 kyu - Printer Errors
# # In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.
# # The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...
# # Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# # You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.
# # The string has a length greater or equal to one and contains only letters from ato z.
# # Examples:
# # s="aaabbbbhaijjjm"
# # printer_error(s) => "0/14"
# # s="aaaxbbbbyyhwawiwjjjwwm"
# # printer_error(s) => "8/22"

# def printer_error(s):
#     return str(len([i for i in s if i > "m"])) + "/" + str(len(s))

# print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))

# 7 kyu - Remove the minimum
# The museum of incredible dull things wants to get rid of some exhibitions.
#  Miriam, the interior architect, comes up with a plan to remove the most
#  boring exhibitions. She gives them a rating, and then removes the one with
#  the lowest rating.
# However, just as she finished rating all exhibitions, she's off to an
#  important fair, so she asks you to write a program that tells her the
#  ratings of the items after one removed the lowest one. Fair enough.
# Task
# Given an array of integers, remove the smallest value. Do not mutate the
#  original array/list. If there are multiple elements with the same value,
#  remove the one with a lower index. If you get an empty array/list, return
#  an empty array/list.
# Don't change the order of the elements that are left.
# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

# def remove_smallest(numbers):
#     a = numbers[:]
#     if a:
#         a.remove(min(a))
#     return a

# print(remove_smallest([1,2,3,4,5])) # [2,3,4,5]
# print(remove_smallest([5,3,2,1,4])) # [5,3,2,4]
# print(remove_smallest([2,2,1,2,1])) # [2,2,2,1]
# print(remove_smallest([])) # []

# 10/02/2024
# 7 kyu - Odd or Even?
# Given a list of integers, determine whether the sum of its elements is odd
#  or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).
# Examples:
# Input: [0]
# Output: "even"
# Input: [0, 1, 4]
# Output: "odd"
# Input: [0, -1, -5]
# Output: "even"

# def odd_or_even(arr):
#     num_sum = 0
#     for num in arr:
#         num_sum += num
#     if num_sum % 2 == 0:
#         return "even"
#     return "odd"

# # def odd_or_even(arr):
# #     return 'even' if sum(arr) % 2 == 0 else 'odd'

# print(odd_or_even([1,2,3,5]))

# 11/02/2024
# 8 kyu - Is he gonna survive?
# A hero is on his way to the castle to complete his mission. However, he's
#  been told that the castle is surrounded with a couple of powerful dragons!
#  each dragon takes 2 bullets to be defeated, our hero has no idea how many
#  bullets he should carry.. Assuming he's gonna grab a specific given number
#  of bullets and move forward to fight another specific given number of
#  dragons, will he survive?
# Return True if yes, False otherwise :)

def hero(bullets, dragons):
    return True if bullets >= dragons * 2 else False

print(hero(10, 5)) # True
print(hero(7, 4)) # False