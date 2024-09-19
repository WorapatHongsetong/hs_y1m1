import math
import random
import os


### Define function convert base10 to base4
def tobase4(num):
    num = int(num)
    temp_storage = 0
    converted = ""


    while True:
        temp_storage = num % 4
        num = num // 4
        converted = str(temp_storage) + converted

        if num < 4:
            converted = str(num) + converted
            break
    

    return converted



### Define function convert base4 to base10
def tobase10(num):
    temp_storage = 0
    converted = 0
    max_digit = len(num)


    for digit, value in enumerate(num):
        temp_storage = int(value) * (4 ** (max_digit - digit - 1))
        converted += temp_storage


    return converted



### Define seeding function
"""
encrypted_character = ("A", "T", "C", "G")

Unique Byte
    100base10
    200base10
"""
def seeding():
    pass



### Character Mapping
char_mapping = {}


for i in range(10):
    char_mapping[str(i)] = i

for i, letter in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    char_mapping[letter] = 10 + i

char_mapping['.'] = 62
char_mapping['@'] = 63

# Char_mapping has 64 character:index pairs
