import math
import random
import os




def add_profile() -> tuple[str, str]:
    """
    When call this function will clear terminal, then recive username and password (both are string).
    Then return tuple of username and password (both are string).
    """


    os.system('cls' if os.name == 'nt' else 'clear')

    print("All inputs must be upper case or lower case latin characters, base10 numbers, \".\" or \"@\"")
    print()

    username = input("  Username: ")
    password = input("  Password: ")

    return username, password




"""
    Begins of Encoder & Decoder Logic
"""




def tobase4(num: int) -> str:
    """
    Convert base 10 number to 4 digit base 4 number.
    """

    remainder = 0
    converted = ""


    while True :
        if num == 0 and len(converted) == 4:
            break


        remainder = num % 4
        num //= 4

        converted = str(remainder) + converted


        if num == 0 and len(converted) < 4:
            converted = "0" + converted
    

    return converted




def tobase10(num: float) -> str:
    """
    Convert 4 digit base 4 number to base 10 number.
    """

    temp_storage = 0
    converted = 0
    max_digit = len(num)


    for digit, value in enumerate(num):
        temp_storage = int(value) * (4 ** (max_digit - digit - 1))
        converted += temp_storage


    return converted




# PEP8 meter.
#         1         2         3         4         5         6         7         8         9        10
#1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890

### Character Mapping
char_mapping = \
{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, \
'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, \
'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, \
'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, 'A': 36, 'B': 37, 'C': 38, 'D': 39, 'E': 40, \
'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 50, \
'P': 51, 'Q': 52, 'R': 53, 'S': 54, 'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59, 'Y': 60, \
'Z': 61, '.': 62, '@': 63}

# Char_mapping has 64 character:index pairs

reverse_char_mapping = \
{0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', \
11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', \
21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', \
31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z', 36: 'A', 37: 'B', 38: 'C', 39: 'D', 40: 'E', \
41: 'F', 42: 'G', 43: 'H', 44: 'I', 45: 'J', 46: 'K', 47: 'L', 48: 'M', 49: 'N', 50: 'O', \
51: 'P', 52: 'Q', 53: 'R', 54: 'S', 55: 'T', 56: 'U', 57: 'V', 58: 'W', 59: 'X', 60: 'Y', \
61: 'Z', 62: '.', 63: '@'}

# Reverse_char_maping has 64 character:index pairs

"""
PS. 
I know that it not in PEP8 format, 
but ending with number that divisable by 10 is so sastisfy.
Please mercy.
"""



### Define decoder function

def encoder(string: str) -> str:
    """
    This function will map each character (using char_mapping) to number and change to 1byte (4 characters in base4).
    """
    
    converted = ""
    max_byte = len(string)


    for i in range(max_byte):
        converted += tobase4(char_mapping[string[i]])


    return converted




### Define decoder function

def decoder(string: str) -> str:
    """
    This function will change 1 byte code (4 characters in base4), and map to reverse_char_mapping, to original character.
    """

    converted = ""
    max_byte = len(string)


    for i in range(0,max_byte,4):
        section = string[i:i+4]
        translation = reverse_char_mapping[int(tobase10(section))]
        converted += translation


    return converted
    



### Define filler function which all 4 neighboring numbers are not forbidden.

def filler_function(num: int) -> str:
    filler = ""
    forbidden = ["1001", "1021", "1101", "1200"]


    for i in range(num):


        while forbidden[0] in filler or forbidden[1] in filler \
            or forbidden[2] in filler or forbidden[3] in filler:

            filler = filler[:(len(filler) - 2)]
            filler += str(random.choice([0, 1, 2, 3]))
            

        filler += str(random.choice([0, 1, 2, 3]))


    return filler




### Detector byte/Forbidden byte

codon_start = tobase4(65)   # 1001
codon_stopt = tobase4(73)   # 1021
codon_userp = tobase4(81)   # 1101
codon_passw = tobase4(96)   # 1200

forbidden = ("1001", "1021", "1101", "1200")




###  Patern and Keys
Patern = (('A', 'T', 'C', 'G'),
 ('A', 'T', 'G', 'C'),
 ('A', 'C', 'T', 'G'),
 ('A', 'C', 'G', 'T'),
 ('A', 'G', 'T', 'C'),
 ('A', 'G', 'C', 'T'),
 ('T', 'A', 'C', 'G'),
 ('T', 'A', 'G', 'C'),
 ('T', 'C', 'A', 'G'),
 ('T', 'C', 'G', 'A'),
 ('T', 'G', 'A', 'C'),
 ('T', 'G', 'C', 'A'),
 ('C', 'A', 'T', 'G'),
 ('C', 'A', 'G', 'T'),
 ('C', 'T', 'A', 'G'),
 ('C', 'T', 'G', 'A'),
 ('C', 'G', 'A', 'T'),
 ('C', 'G', 'T', 'A'),
 ('G', 'A', 'T', 'C'),
 ('G', 'A', 'C', 'T'),
 ('G', 'T', 'A', 'C'),
 ('G', 'T', 'C', 'A'),
 ('G', 'C', 'A', 'T'),
 ('G', 'C', 'T', 'A'))

Key = ('ATCCCAGGGGGG',
 'ATGGGACCCCCC',
 'ACTCCCAGGGGG',
 'ACTGGGACCCCC',
 'AGTCCCAGGGGG',
 'AGTGGGACCCCC',
 'TACCCCAGGGGG',
 'TAGGGACCCCCC',
 'TCCCCAAGGGGG',
 'TCCGGGACCCCC',
 'TGGGGACCCCCC',
 'TGCCCACCCGGG',
 'CATCCCAGGGGG',
 'CATGGGACCCCC',
 'CTACCCAGGGGG',
 'CTGGGACCCCCC',
 'CGACCCAGGGGG',
 'CGTGGGACCCCC',
 'GACCCCAGGGGG',
 'GATGGGACCCCC',
 'GCACCCAGGGGG',
 'GCTGGGACCCCC',
 'GTACCCAGGGGG',
 'GTGGGACCCCCC')
# 12 characters each.

### All elements of Patern and Key are unique.




### Define 

print("lol")
input()
