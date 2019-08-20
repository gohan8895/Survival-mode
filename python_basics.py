# import pygame
from math import sqrt
from os import path
import operator

# Waypoin 1: Say Greeting
def hello(name):
    return "Hello " + name.strip() + "!"
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
#         ('Hotel Grand Saigon', 120),
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
        sum = 0
        for i in range(len(points) - 1):
            for j in range(i+1, len(points), 1):
                dis = calculate_euclidean_distance_between_2_points(points[i] \
                ,points[j])
                sum += dis
        return sum
    else:
        raise ValueError('The list MUST contain at least 2 points')
# Test wp8
# print(calculate_euclidean_distance_between_points([(0, 0), (3, 4)]))
# print(calculate_euclidean_distance_between_points([(0, 0), (3, 4), (0, 0)]))
# print(calculate_euclidean_distance_between_points([(0, 0), (3, 4), (-1, -1)]))
# print(calculate_euclidean_distance_between_points([]))
# print(calculate_euclidean_distance_between_points([(1, 1)]))


# Waypoint 9: Capitalize the Words of a String
def capitalize_words(s):
    pass


# Waypoint 10: Uppercase and Lowercase Words
def uppercase_lowercase_words(s):
    pass


# Waypoint 11: Factorial
def factorial(n):
    pass


# Waypoint 12: Convert a Digit Character to an Integer
def char_to_int(c):
    pass


# Waypoint 13: Convert a String of Digit Characters to an Integer
def string_to_int(s):
    pass


# Waypoint 14: Test Palindrome String
def is_palindrome(value):
    pass


# Waypoint 15: Convert Roman Numerals to Integer
# Python Function to Return the Numerical Value of a Roman Numeral
def roman_numeral_to_int(roman_numeral):
    pass


# Waypoint 16: Play a Melody
def play_melody(melody, sound_basedir):
    melody_no_sharp = []
    flat = {'c': 'db', 'd': 'eb', 'f': 'gb', 'g': 'ab', 'a': 'bb'}
    for i in melody:
        if '#' in i:
            note = path.join(sound_basedir,
                             flat[i.lower()[0]]+i[-1]+'.ogg')
            melody_no_sharp.append(note)
        else:
            note = path.join(sound_basedir, i.lower() + '.ogg')
            melody_no_sharp.append(note)
    pygame.init()
    for i in melody_no_sharp:
        sound = pygame.mixer.Sound(i)
        channel = sound.play()
        clock = pygame.time.Clock().tick(1.234567890)
        channel = sound.stop()
    pygame.quit()


# MELODY_HAPPY_BIRTHDAY_TO_YOU = (
#     'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
#     'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
#     'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
#     'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4',
# )
# MELODY_FUR_ELISE = (
#     'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
#     'C4', 'E4', 'A4', 'B4',
#     'E4', 'Ab4', 'B4', 'C5',
#     'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
#     'C4', 'E4', 'A4', 'B4',
#     'E4', 'C5', 'B4', 'A4',
#     'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
#     'C4', 'E4', 'A4', 'B4',
#     'E4', 'Ab4', 'B4', 'C5',
#     'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
#     'C4', 'E4', 'A4', 'B4',
#     'E4', 'C5', 'B4', 'A4',
