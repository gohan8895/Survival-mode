import pygame
from os import path
# Waypoin 1: Say Greeting
def hello(name):
    print("Hello" + name + "!")


# Waypoin 2: Pythagorean Theorem
def calculate_hypotenuse(a, b):
    return a**b*0.5


# Waypoint 3: Test whether all Conditions are True
def are_all_conditions_true(conditions):
    pass


# Waypoint 4: Test whether at least one Condition is True
def is_a_condition_true(conditions):
    pass


# Waypoint 5: Filter List of Integers
def filter_integers_greater_than(l, n):
    pass


# Waypoint 6: Find Cheapest Hotels
def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    pass


# Waypoint 7: Calculate Distance between two 2D Points
def calculate_euclidean_distance_between_2_points(p1, p2):
    pass


# Waypoint 8: Calculate Distance between several 2D Points
def calculate_euclidean_distance_between_points(points):
    pass


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
