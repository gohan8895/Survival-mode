#!/usr/bin/python3
import pygame
# from math import sqrt
import string
import time

# Waypoin 1: Say Greeting
def hello(name):
    return "Hello " + ' '.join(name.strip().split()) + "!"
# Test wp1
# name = input('what\'s your name? ')
# print(hello(name))


# Waypoin 2: Pythagorean Theorem
def calculate_hypotenuse(a, b):
    return (a*a + b*b)**0.5
# Test wp2
# print(calculate_hypotenuse(1,1))
# print(calculate_hypotenuse(3,4))
# print(calculate_hypotenuse(8,10))


# Waypoint 3: Test whether all Conditions are True
def are_all_conditions_true(conditions):
    return None if not conditions else not False in conditions
# Test wp3
# print(are_all_conditions_true([True, True, False, True, False, False, True]))
# print(are_all_conditions_true([True, True, True]))
# print(are_all_conditions_true([]))


# Waypoint 4: Test whether at least one Condition is True
def is_a_condition_true(conditions):
    return None if not conditions else True in conditions
# Test wp4
# print(is_a_condition_true([True, True, False, True, False, False, True]))
# print(is_a_condition_true([True, True, True]))
# print(is_a_condition_true([False, False]))
# print(is_a_condition_true([]))


# Waypoint 5: Filter List of Integers
def filter_integers_greater_than(l, n):
    return [num for num in l if num > n]
# Test wp5
# l = [0, 3, 5, -2, 9, 8]
# print(filter_integers_greater_than(l, 4))
# print(filter_integers_greater_than(l, 6))


# Waypoint 6: Find Cheapest Hotels
def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    hotel_daily_rates = sorted(hotel_daily_rates, key = lambda tup: tup[1])
    return [hotel_daily_rates[i][0] for i in range(len(hotel_daily_rates)) \
    if hotel_daily_rates[i][1] <= maximum_daily_rate]
# Test wp6
# hotel_daily_rates = [
#         ('Majestic Saigon Hotel', 93),
#         ('Hotel Grand Saigon', 1translate(None, "!?.,' '")20),
#         ('Sofitel Saigon Plaza', 123),
#         ('Hotel Continental', 62),
#         ('Caravelle Hotel', 180),
#         ('Sheraton Saigon Hotel', 216),
#         ('Park Hyatt Saigon', 209)
#     ]
# print(find_cheapest_hotels(hotel_daily_rates, 50))
# print(find_cheapest_hotels(hotel_daily_rates, 85))
# print(find_cheapest_hotels(hotel_daily_rates, 150))


# Waypoint 7: Calculate Distance between two 2D Points
def calculate_euclidean_distance_between_2_points(p1, p2):
    return calculate_hypotenuse(p2[0] - p1[0], p2[1] - p1[1])
# Test wp7
# print(calculate_euclidean_distance_between_2_points((1, 2), (1, 2)))
# print(calculate_euclidean_distance_between_2_points((0, 0), (3, 4)))
# print(calculate_euclidean_distance_between_2_points((1, 1), (2, 2)))


# Waypoint 8: Calculate Distance between several 2D Points
def calculate_euclidean_distance_between_points(points):
    if len(points) >= 2:
        return sum(calculate_euclidean_distance_between_2_points(points[i],\
        points[i+1]) for i in range(len(points)-1))
    else:
        raise ValueError('The list MUST contain at least 2 points')
# Test wp8
# print(calculate_euclidean_distance_between_points([(0, 0), (3, 4)]))
# print(calculate_euclidean_dipygamestance_between_points([(0, 0), (3, 4), (0, 0)]))
# print(calculate_euclidean_distance_between_points([(0, 0), (3, 4), (-1, -1)]))
# print(calculate_euclidean_distance_between_points([]))
# print(calculate_euclidean_distance_between_points([(1, 1)]))


# Waypoint 9: Capitalize the Words of a String
def capitalize_words(s):
    if type(s) is str:
        return ' '.join(word.capitalize() for word in s.strip().split())
    elif s is None:
        return None
    else:
        raise TypeError('Not a string')
# Test wp9
# print(capitalize_words('hello, word!'))
# print(capitalize_words('JACK CARVER'))
# print('   ')
# print(capitalize_words('Không  có gì    quý hơn  độc lập      tự do'))
# print(capitalize_words(None))
# print(capitalize_words(69))


# Waypoint 10: Uppercase and Lowercase Words
def uppercase_lowercase_words(s):
    if type(s) is str:
        s = s.split()
        for i in range(len(s)):
            if i%2:
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()
        return ' '.join(s)
    elif s is None:
        return None
    else:
        raise TypeError('Not a string')
# Test wp10
# print(uppercase_lowercase_words('one two three four five'))
# print(uppercase_lowercase_words('SIX SEVEN EIGHT NINE TEN'))
# print(uppercase_lowercase_words('1 one two 2 3 three four 4 five six'))
# print(uppercase_lowercase_words('   '))
# print(uppercase_lowercase_words(None))
# print(uppercase_lowercase_words(69))


# Waypoint 11: Factorial
def factorial(n):
    try:
        if n < 0:
            raise ValueError('Not a positive integer')
        res = 1
        for i in range(1,n+1,1):
            res *= i
        return res
    except TypeError:
        raise TypeError('Not an integer')
# Test wp11
# print([(n, factorial(n)) for n in range(6)])
# print(factorial('3'))
# print(factorial(-2))


# Waypoint 12: Convert a Digit Character to an Integer
def char_to_int(c):
    try:
        if len(c) != 1 or c not in string.digits:
            raise ValueError('Not a single digit')
        return ord(c) - 48
    except TypeError:
        raise TypeError('Not a string')
# Test wp12
# print(char_to_int('9'))
# print(char_to_int(None))
# print(char_to_int(13.4))
# print(char_to_int('12'))


# Waypoint 13: Convert a String of Digit Characters to an Integer
def string_to_int(s):
    try:
        return int(''.join(str(num) for num in [char_to_int(c) for c in s]))
    except ValueError:
        raise ValueError('Not a positive integer string expression')
    except TypeError:
        raise TypeError('Not a string')
# Test wp13
# print(string_to_int('17049171'))
# print(string_to_int(None))
# print(string_to_int(1984))
# print(string_to_int('123abcd'))
# print(string_to_int('-1234'))


# Waypoint 14: Test Palindrome String
def is_palindrome(value):
    value = ''.join(char.lower() for char in str(value) if char.isalnum())
    return value[::-1] == value
# Test wp14
# print(is_palindrome('ma d am'))
# print(is_palindrome('racecar'))
# print(is_palindrome(10801))
# print(is_palindrome(1.947491))
# print(is_palindrome(1984))
# print(is_palindrome('Hello, word!'))
# print(is_palindrome('A man, a plan, a canal, Panama!'))
# print(is_palindrome('Was it a car or a cat I saw?'))
# print(is_palindrome("No 'x' in Nixon"))


# Waypoint 15: Convert Roman Numerals to Integer
def roman_numeral_to_int(roman_numeral):
    try:
        roman_symbol_value = {"N": 0,
                              "I": 1,
                              "V": 5,
                              "X": 10,
                              "L": 50,
                              "C": 100,
                              "D": 500,
                              "M": 1000
                              }
        result = 0
        for i in range(len(roman_numeral) - 1):
            if roman_symbol_value[roman_numeral[i]] <\
               roman_symbol_value[roman_numeral[i+1]]:
                result -= roman_symbol_value[roman_numeral[i]]
            else:
                result += roman_symbol_value[roman_numeral[i]]
        result += roman_symbol_value[roman_numeral[-1]]
        return result
    except (ValueError, KeyError):
        raise ValueError("Not a Roman numeral")
    except TypeError:
        raise TypeError("Not a string")
# Test wp15
# print(roman_numeral_to_int('XXXIX'))
# print(roman_numeral_to_int('CCXLVI'))
# print(roman_numeral_to_int('DCCLXXXIX'))
# print(roman_numeral_to_int('MMCDXXI'))
# print(roman_numeral_to_int('CLX'))
# print(roman_numeral_to_int('CCVII'))
# print(roman_numeral_to_int('MIX'))
# print(roman_numeral_to_int('MLXVI'))
# print(roman_numeral_to_int('MDCCLXXVI'))
# print(roman_numeral_to_int('MCMLIV'))
# print(roman_numeral_to_int('MMXIV'))
# print(roman_numeral_to_int('MMMCMXCIX'))
# print(roman_numeral_to_int(1234))
# print(roman_numeral_to_int('XYZ'))


# Waypoint 16: Play a Melody
def play_melody(melody, sound_basedir):
    sharp_to_flat = {'c#': 'db',
                     'd#': 'eb',
                     'f#': 'gb',
                     'g#': 'ab',
                     'a#': 'bb'
                     }
    melody_path_name = []
    for note in melody:
        if "#" in note:
            note = sound_basedir + '/' + sharp_to_flat[note[:2].lower()] + \
            note[-1] + ".ogg"
            melody_path_name.append(note)
        else:
            note = sound_basedir + '/' + note.lower() + ".ogg"
            melody_path_name.append(note)
    for note in melody_path_name:
        pygame.init()
        sound = pygame.mixer.Sound(note)
        channel = sound.play()
        pygame.time.delay(400)
        channel = sound.stop()
    return melody_path_name
MELODY_I_LOVE_YOU = [
        'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
        'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
        'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
        'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
        'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
        'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
        'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
        'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3'
        ]
print(play_melody(MELODY_I_LOVE_YOU, './sounds/piano'))

# MELODY_HAPPY_BIRTHDAY_TO_YOU = (
#     'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
#     'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
#     'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
#     'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4')
# print(play_melody(MELODY_HAPPY_BIRTHDAY_TO_YOU, './sounds/piano'))
