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




### Detector byte/Forbidden byte

codon_start = tobase4(65)   # 1001
codon_stopt = tobase4(73)   # 1021
codon_userp = tobase4(81)   # 1101
codon_passw = tobase4(96)   # 1200

forbidden = ("1001", "1021", "1101", "1200")




### Define filler function which all 4 neighboring numbers are not forbidden.
def filler_function(num):
    filler = ""
    forbidden = ["1001", "1021", "1101", "1200"]


    for i in range(num):


        while forbidden[0] in filler or forbidden[1] in filler \
            or forbidden[2] in filler or forbidden[3] in filler:

            filler = filler[:(len(filler) - 2)]
            filler += str(random.choice([0, 1, 2, 3]))
            

        filler += str(random.choice([0, 1, 2, 3]))


    return filler




### Character Mapping
char_mapping = {}

for i in range(10):
    char_mapping[str(i)] = i

for i, letter in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    char_mapping[letter] = 10 + i

char_mapping['.'] = 62
char_mapping['@'] = 63

# Char_mapping has 64 character:index pairs




def encoder(string):
    string = str(string)
    converted = ""
    max_byte = len(string)


    for i in range(max_byte):
        converted += tobase4(char_mapping[string[i]])


    return converted




def decoder(string):
    string = str(string)
    converted = ""
    
    





###  Patern and Keys
Patern = (['A', 'T', 'C', 'G'],
 ['A', 'T', 'G', 'C'],
 ['A', 'C', 'T', 'G'],
 ['A', 'C', 'G', 'T'],
 ['A', 'G', 'T', 'C'],
 ['A', 'G', 'C', 'T'],
 ['T', 'A', 'C', 'G'],
 ['T', 'A', 'G', 'C'],
 ['T', 'C', 'A', 'G'],
 ['T', 'C', 'G', 'A'],
 ['T', 'G', 'A', 'C'],
 ['T', 'G', 'C', 'A'],
 ['C', 'A', 'T', 'G'],
 ['C', 'A', 'G', 'T'],
 ['C', 'T', 'A', 'G'],
 ['C', 'T', 'G', 'A'],
 ['C', 'G', 'A', 'T'],
 ['C', 'G', 'T', 'A'],
 ['G', 'A', 'T', 'C'],
 ['G', 'A', 'C', 'T'],
 ['G', 'T', 'A', 'C'],
 ['G', 'T', 'C', 'A'],
 ['G', 'C', 'A', 'T'],
 ['G', 'C', 'T', 'A'])

Key = ('ATCCCAGGGGGG',
 'ATGGGACCCCCC',
 'ACTCCCAGGGGG',
 'ACTGGGACCCCCC',
 'AGTCCCAGGGGG',
 'AGTGGGACCCCCC',
 'TACCCCAGGGGG',
 'TAGGGACCCCCC',
 'TCCCCAAGGGGG',
 'TCCGGGACCCCCC',
 'TGGGGACCCCCC',
 'TGCCCACCCGGGG',
 'CATCCCAGGGGG',
 'CATGGGACCCCCC',
 'CTACCCAGGGGG',
 'CTGGGACCCCCC',
 'CGACCCAGGGGG',
 'CGTGGGACCCCCC',
 'GACCCCAGGGGG',
 'GATGGGACCCCCC',
 'GCACCCAGGGGG',
 'GCTGGGACCCCCC',
 'GTACCCAGGGGG',
 'GTGGGACCCCCC')

user = "English"
password = "Password12345678"

print(encoder(user))
print(encoder(password))