import math
import random
import os




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

char_valid = \
('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',\
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',\
 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '@')


### Detector byte/Forbidden byte

Codon_start = "1001"            # 65
Codon_stopt = "1021"            # 73
Codon_userp = "1101"            # 81
Codon_passw = "1200"            # 96

Forbidden = ("1001", "1021", "1101", "1200")




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




def encoder(string: str) -> str:
    """
    This function will map each character (using char_mapping) to number and change to 1byte (4 characters in base4).
    """
    
    converted = ""
    max_byte = len(string)


    for i in range(max_byte):
        converted += tobase4(char_mapping[string[i]])


    return converted




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
    



def filler_function(num: int) -> str:
    """
    When call this function, it will create sequence of number in base4 (string) that have lenght of input num (int).
    Which random sequence of number will not contains forbidden section ("1001", "1021", "1101", "1200").
    Then return that sequnce (string).
    """


    filler = ""
    forbidden = ["1001", "1021", "1101", "1200"]


    for i in range(num):


        while forbidden[0] in filler or forbidden[1] in filler \
            or forbidden[2] in filler or forbidden[3] in filler:

            filler = filler[:(len(filler) - 2)]
            filler += str(random.choice([0, 1, 2, 3]))
            

        filler += str(random.choice([0, 1, 2, 3]))


    return filler




def completeter(username1: str, password1: str) -> tuple[str, str]:
    """
    Complete encoded username and password with start, stop and type codon.
    """

    username2 = Codon_start + Codon_userp + username1 + Codon_stopt
    password2 = Codon_start + Codon_passw + password1 + Codon_stopt

    return username1, password2




def encrypter(username2: str, password2: str) -> str:
    """
    Randomly combine username and password into string, add filler to fill the string until string's lenght is 256(64 byte).
    """
    #           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
    position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    




def decrypter(encrypted: str) -> tuple[str, str]:
    pass
    












### Interfaces and User inputs

def add_profile() -> tuple[str, str, str, bool]:
    """
    When call this function will clear terminal, then recive username, password and usernote (those are string).
    Then return tuple of username, password and usernote (those are string).
    """

    reject = False

    os.system('cls' if os.name == 'nt' else 'clear')

    print("All inputs must be upper case or lower case latin characters, base10 numbers, \".\" or \"@\"")
    print()

    username = input("  Username (Maximum 16 Characters): ")
    password = input("  Password (Maximum 16 Characters): ")
    usernote = input("  UserNote : ")
    print()
    input("-Enter to continue-")


    # Empty String Error
    if len(username) == 0 or len(password) == 0:
        reject = True
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Error : Empty String")
        print()
        input("-Enter to continue-")

    # 
    if len(username) > 16 or len(password) > 16:
        reject = True
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Error : Lenght")
        print()
        input("-Enter to continue-")


    for character in username:

        if character not in char_valid:
            reject = True
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Error : Invalid Character(s)")
        print()
        input("-Enter to continue-")
    

    for character in password:

        if character not in char_valid:
            reject = True
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Error : Invalid Character(s)")
        print()
        input("-Enter to continue-")



    return username, password, usernote, reject



# print(encrypter("english123456", "Password123456"))
# print(len(encrypter("english123456", "Password123456")))
# encrypted = encrypter("english123456", "Password123456")
# print("1001" in encrypted, "1021" in encrypted, "1101" in encrypted, "1200" in encrypted)

add_profile()