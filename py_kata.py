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

# 08/01/2024
# 7 kyu - Sum of odd numbers
# Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting
#  at index 1) e.g.: (Input --> Output)
# 1 -->  1
# 2 --> 3 + 5 = 8
# 3 --> 7 + 9 + 11 = 27

# def row_sum_odd_numbers(n):
#     return n**3

# print(row_sum_odd_numbers(3))

# # 09/01/2024
# # 7 kyu - Printer Errors
# # In a factory a printer prints labels for boxes. For one kind of boxes the
#  printer has to use colors which, for the sake of simplicity, are named with
#   letters from a to m.
# # # The colors used by the printer are recorded in a control string. For
#  example a "good" control string would be aaabbbbhaijjjm meaning that the
# printer used three times color a, four times color b, one time color h then
# one time color a...
# # # Sometimes there are problems: lack of colors, technical malfunction and
#  a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters
# not from a to m.
# # # You have to write a function printer_error which given a string will
#  return the error rate of the printer as a string representing a rational
# whose numerator is the number of errors and the denominator the length of
# the control string. Don't reduce this fraction to a simpler expression.
# # # The string has a length greater or equal to one and contains only
#  letters from ato z.
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

# 10/01/2024
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

# 11/01/2024
# 8 kyu - Is he gonna survive?
# A hero is on his way to the castle to complete his mission. However, he's
#  been told that the castle is surrounded with a couple of powerful dragons!
#  each dragon takes 2 bullets to be defeated, our hero has no idea how many
#  bullets he should carry.. Assuming he's gonna grab a specific given number
#  of bullets and move forward to fight another specific given number of
#  dragons, will he survive?
# Return True if yes, False otherwise :)

# Function to check if hero can survive
# def hero(bullets, dragons):
#     return True if bullets >= dragons * 2 else False

# print(hero(10, 5)) # True
# print(hero(7, 4)) # False

# 12/01/2024
# 7 kyu - Vowel Count
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.

# def get_count(input_str):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     vowel_count = 0
#     for char in input_str:
#         if char in vowels:
#             vowel_count += 1
#     return vowel_count

# print(get_count('pill'))


# 14/01/2024
# 8 kyu - Beginner Series #4 Cockroach
# The cockroach is one of the fastest insects. Write a function which takes
#  its speed in km per hour and returns it in cm per second, rounded down to
#  the integer (= floored).
# For example:
# 1.08 --> 30
# Note! The input is a Real number (actual type is language dependent) and is
#  >= 0. The result should be an Integer.

# def cockroach_speed(s):
#     return int(s*100000/3600)

# print(cockroach_speed(1.08))

# 7 kyu - Is this a triangle?
# Implement a method that accepts 3 integer values a, b, c. The method should
#  return true if a triangle can be built with the sides of given length and
#  false in any other case.
# (In this case, all triangles must have surface greater than 0 to be
#  accepted).
# Examples:
# Input -> Output
# 1,2,2 -> true
# 4,2,3 -> true
# 2,2,2 -> true
# 1,2,3 -> false
# -5,1,3 -> false
# 0,2,3 -> false
# 1,2,9 -> false

# def is_triangle(a, b, c):
#     return (a + b) > c and (b + c) > a and (c + a) > b

# print(is_triangle(4,2,3))

# 15/01/2024
# 8 kyu - Transportation on vacation
# After a hard quarter in the office you decide to get some rest on a vacation.
# So you will book a flight for you and your girlfriend and try to leave all
# the mess behind you.
# You will need a rental car in order for you to get around in your vacation.
# The manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more
# days, you get $50 off your total. Alternatively, if you rent the car for 3
# or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).

# def rental_car_cost(d):
#     total = 40 * d
#     if d >= 7:
#         return total - 50
#     if 3 <= d <7:
#         return total - 20
#     return total

# print(rental_car_cost(2)) # 80
# print(rental_car_cost(7)) # 230
# print(rental_car_cost(3)) # 100


# 16/01/2024
# 8 kyu - Calculate average
# Write function avg which calculates average of numbers in given list.
# Note: Empty arrays should return 0.

# def find_average(array):
#     return sum(array)/len(array) if array else 0

# print(find_average([1,2,3,4,5])) # 3
# print(find_average([1,1,1,1,1,1,1,2])) # 1.125
# print(find_average([])) # 0

# # 17/01/2024
# # 7 kyu - Square Every Digit
# # Welcome. In this kata, you are asked to square every digit of a number and
# #  concatenate them.
# # For example, if we run 9119 through the function, 811181 will come out,
# #  because 9^2 is 81 and 1^2 is 1.
# # Note: The function accepts an integer and returns an integer

# def square_digits(num):
#     return int(''.join(str(int(i)**2) for i in str(num)))

# print(square_digits(9119)) # 811181
# print(square_digits(0)) # 0

# Copilot kata using list comprehension:
# Given a list of numbers, write a function square_odd_numbers that returns a
# new list containing the squares of all the odd numbers in the original list.

# def square_odd_numbers(numbers):
#     return [n**2 for n in numbers if n%2 != 0]

# print(square_odd_numbers([1, 2, 3, 4, 5, 6]))

# 18/01/2024
# 7 kyu - Friend or Foe?
# Make a program that filters a list of strings and returns a list with only
#  your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a
#  friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
# i.e.
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

# def friend(x):
#     return [name for name in x if len(name) == 4]

# print(friend(["Ryan", "Kieran", "Mark"]))

# 19/01/2024
# 8 kyu - What is between?
# Complete the function that takes two integers (a, b, where a < b) and return
#  an array of all integers between the input parameters, including them.
# For example:
# a = 1
# b = 4
# --> [1, 2, 3, 4]

# def between(a,b):
#     return list(range(a, b+1))

# print(between(1,4))

# 21/01/2024
# 8 kyu - Function 2 - squaring an argument
# Now you have to write a function that takes an argument and returns the
#  square of it.

# def square(n):
#     return n ** 2

# print(square(4))

# 22/01/2024
# 7 kyu - Testing 1-2-3
# Your team is writing a fancy new text editor and you've been tasked with
#  implementing the line numbering.
# Write a function which takes a list of strings and returns each line
#  prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and
#  space in between.
# Examples:
# number([]) # => []
# number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]

# def number(lines):
#     return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

#     # return [n for n in lines]

# print(number(['a', 'b', 'c']))


# 23/01/2024
# 8 kyu - Double Char
# Given a string, you have to return a string in which each character
#  (case-sensitive) is repeated once.
# double_char("String") ==> "SSttrriinngg"
# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
# double_char("1234!_ ") ==> "11223344!!__  "

# def double_char(s):
#     return ''.join([n * 2 for n in s])

# print(double_char("String"))

# 24/01/2024
# 7 kyu - Disemvowel Trolls
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from
#  the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string
#  with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths
#  wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

# my code
# def disemvowel(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     newstring = [letter for letter in string if letter.lower() not in vowels]
#     newstring = ''.join(newstring)
#     return newstring

# # best code
# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s

# print(disemvowel('testing'))

# 25/01/2024
# 8 kyu - Removing Elements
# Take an array and remove every second element out of that array. Always keep
#  the first element and start removing with the next element.
# Example:
# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
# None of the arrays will be empty, so you don't have to worry about that!

# def remove_every_other(my_list):
#     return my_list[::2]

# print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))

# 26/01/2024
# 8 kyu - Keep Hydrated!
# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres
#  of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres
#  Nathan will drink, rounded to the smallest value.
# For example:
# time = 3 ----> litres = 1
# time = 6.7---> litres = 3
# time = 11.8--> litres = 5

# def litres(time):
#     import math as m
#     return m.floor(0.5 * time)

# print(litres(3))

# 27/01/2024
# 8 kyu - Switch it Up!
# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".
# Try using "Switch" statements.

# # my code:
# def switch_it_up(number):
#     switcher = {
#         0: 'Zero',
#         1: 'One',
#         2: 'Two',
#         3: 'Three',
#         4:'Four',
#         5:'Five',
#         6:'Six',
#         7:'Seven',
#         8:'Eight',
#         9:'Nine'
#     }
#     return switcher.get(number)

# best code:
# def switch_it_up(number):
#     return ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"][number]

# print(switch_it_up(1))

# 28/01/2024
# 7 kyu - Highest and Lowest
# In this little assignment you are given a string of space separated numbers,
#  and have to return the highest and lowest number.
# Example:
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space,
#  and highest number is first.

# def high_and_low(numbers):
#     numbers = numbers.split()
#     numbers = [int(n) for n in numbers]
#     return f"{max(numbers)} {min(numbers)}"
#     # return "{} {}".format(max(numbers), min(numbers))

# print(high_and_low("1 2 3 4 5")) # return "5 1"

# 29/01/2024
# 8 kyu - Parse nice int from char problem
# You ask a small girl,"How old are you?" She always says, "x years old",
# where x is a random number between 0 and 9.

# Write a program that returns the girl's age (0-9) as an integer.

# Assume the test input string is always a valid string. For example, the test
# input may be "1 year old" or "5 years old". The first character in the string
# is always a number.

# def get_age(age):
#     return int(age[0])

# print(get_age('5 years old'))

# 31/01/2024
# 6 kyu - Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *
# Python: return a list;
# Have fun!
# for example, a tower of 3 floors looks like below
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]

# def tower_builder(n_floors):
#     tower = []
#     for i in range(1, n_floors+1):
#         tower.append(' ' * (n_floors-i) + '*' * (2*i-1) + ' ' * (n_floors-i))
#     return tower

# print(tower_builder(2))

# extra practice:
# diamond maker
# def diamond_maker(n):
#     if n % 2 == 0 or n < 1:
#         return None
#     diamond = []
#     for i in range(1, n//2+2):
#         diamond.append(' ' * (n-i) + '*' * (2*i-1) + ' ' * (n-i))
#     for i in range(n//2, 0, -1):
#         diamond.append(' ' * (n-i) + '*' * (2*i-1) + ' ' * (n-i))
#     return diamond

# print(diamond_maker(5))

# 03/02/2024

# 6 kyu - Unique In Order
# Implement the function unique_in_order which takes as argument a sequence and
#  returns a list of items without any elements with the same value next to
#  each other and preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# def unique_in_order(iterable):
#     unique = []
#     for i in iterable:
#         if len(unique) == 0 or i != unique[-1]:
#             unique.append(i)
#     return unique

# print(unique_in_order('AAAABBBCCDAABBB')) # ['A', 'B', 'C', 'D', 'A', 'B']

# 04/02/2024
# 6 kyu - Your order, please
# Your task is to sort a given string. Each word in the string will contain a
#  single number. This number is the position the word should have in the
#  result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input
#  String will only contain valid consecutive numbers.
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"

# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int("".join(filter(str.isdigit, x)))))

# print(order("is2 Thi1s T4est 3a")) # "Thi1s is2 3a T4est"


# 07/02/2024
# 8 kyu - Abbreviate a Two Word Name
# Write a function to convert a name into initials. This kata strictly takes
#  two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# Patrick Feeney => P.F

# def abbrev_name(name):
#     return ".".join([i[0].upper() for i in name.split()])

# print(abbrev_name('Dave Thingy thing'))


# 08/02/2024
# 8 kyu - Difference of Volumes of Cuboids
# In this simple exercise, you will create a program that will take two lists
#  of integers, a and b. Each list will consist of 3 positive integers above 0,
#  representing the dimensions of cuboids a and b. You must find the difference
#  of the volumes of cuboids a and b. The volume of a cuboid is the product of
#  its dimensions.
# Example:
# If the parameters are two lists of three integers each: [1, 2, 3], [2, 3, 4],
#  the volume of a is 6 and the volume of b is 24. Therefore, the function
#  should return 18.

# my code:
# def find_difference(a, b):
#     if a[0]*a[1]*a[2] > b[0]*b[1]*b[2]:
#         return a[0]*a[1]*a[2] - b[0]*b[1]*b[2]
#     return b[0]*b[1]*b[2] - a[0]*a[1]*a[2]

# print(find_difference([1, 2, 3], [2, 3, 4]))

# # best code:
# from numpy import prod

# def find_difference(a, b):
#     return abs(prod(a) - prod(b))


# 10/02/2024
# 7 kyu - String ends with?
# Complete the solution so that it returns true if the first argument(string)
#  passed in ends with the 2nd argument (also a string).
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# def solution(string, ending):
#     return string.endswith(ending)

# print(solution('abc', 'bc'))


# 12/02/2024
# 7 kyu - Exes and Ohs
# Check to see if a string has the same amount of 'x's and 'o's. The method
#  must return a boolean and be case insensitive. The string can contain any
#  char.
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# my code
# def xo(s):
#     lowers = s.lower()
#     xs = ''
#     os = ''
#     for letter in lowers:
#         if letter == 'x':
#             xs += 'x'
#         if letter == 'o':
#             os += 'y'
#     return len(xs) == len(os)

# # best code
# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

# print(xo('OoxX'))

# 14/02/2024
# 8 kyu - Correct the mistakes of the character recognition software
# Character recognition software is widely used to digitise printed texts.
#  Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are
#  digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to
#  handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

# def correct(string):
#     return string.replace('5', 'S').replace('0', 'O').replace('1', 'I')

# print(correct('5tr1ng'))

# 20/02/2024
# 8 kyu - Square(n) Sum
# Complete the square sum function so that it squares each number passed into
#  it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

# my code
# def square_sum(numbers):
#     total = 0
#     for n in numbers:
#         total += n*n
#     return total

# # best code
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)

# print(square_sum([1, 2, 2]))


# 10/04/2024

# 7 kyu - Reverse words
# Complete the function that accepts a string parameter, and reverses each word
#  in the string. All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod secaps"

# def reverse_words(text):
#     return ' '.join([word[::-1] for word in text.split(' ')])

# print(reverse_words('This is an example!'))

# 11/04/2024
# 8 kyu - Opposites Attract

# Timmy & Sarah think they are in love, but around where they live, they will
#  only know once they pick a flower each. If one of the flowers has an even
#  number of petals and the other has an odd number of petals it means they
#  are in love.
# Write a function that will take the number of petals of each flower and
#  return true if they are in love and false if they aren't.

# def lovefunc(flower1, flower2):
#     return (flower1+flower2) % 2 != 0

# print(lovefunc(2,2))

# 7 kyu - Two to One
# Take 2 strings s1 and s2 including only letters from a to z. Return a new
#  sorted string, the longest possible, containing distinct letters,
#  each taken only once - coming from s1 or s2.
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

def longest(S1, S2):
    return ''.join(sorted(set(S1+S2)))

print(longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq'))
