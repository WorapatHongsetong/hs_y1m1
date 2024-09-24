def tobase4(number):
    number = int(number)
    remainder = 0
    converted = ""


    while True :
        if number == 0 and len(converted) == 4:
            break


        remainder = number % 4
        number //= 4

        converted = str(remainder) + converted


        if number == 0 and len(converted) < 4:
            converted = "0" + converted
    

    return converted




def tobase10(num):
    temp_storage = 0
    converted = 0
    max_digit = len(num)


    for digit, value in enumerate(num):
        temp_storage = int(value) * (4 ** (max_digit - digit - 1))
        converted += temp_storage


    return converted




### Character Mapping
char_mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, \
                'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, \
                'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, \
                'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, 'A': 36, 'B': 37, 'C': 38, 'D': 39, 'E': 40, \
                'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 50, \
                'P': 51, 'Q': 52, 'R': 53, 'S': 54, 'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59, 'Y': 60, \
                'Z': 61, '.': 62, '@': 63}

# Char_mapping has 64 character:index pairs




def encoder(string):
    converted = ""
    max_byte = len(string)


    for i in range(max_byte):
        converted += tobase4(char_mapping[string[i]])


    return converted




# def decoder(string):
string = "12342234323442345234"
converted = ""
max_byte = len(string)


# for i in range(0,max_byte,4):
#     section = [string[i:i+4]]
#     translation = 
#     converted += translation

print(converted)
    






user = "EnglishHunter360Assassin2014"

user_encoded = encoder(user)

print(user_encoded)