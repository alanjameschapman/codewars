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