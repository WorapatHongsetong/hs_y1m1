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
('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',\
 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',\
 'Y', 'Z', '.', '@')


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






### Basic Function

def tobase4(num: int) -> str:
    """
    Convert base10 integer to 4 digit base4 string.

    Arg:
        num (int) - base10 interger

    Return: 
        converted (str) - 4 digit base4 string

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




def tobase10(num: str) -> int:
    """
    Convert 4 digit base4 string to base10 integer.

    Arg:
        num (str) - 4 digit base4 string.

    Return:
        converted (int) - base10 integer.
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
    Convert sequence of character to base4 string.

    Arg:
        string (str) - sequence of character (0-9, a-z, A-Z, ., @).
    
    Return:
        converted (str) - base4 number represent original input.
    """
    
    converted = ""
    max_byte = len(string)


    for i in range(max_byte):
        converted += tobase4(char_mapping[string[i]])


    return converted




def decoder(string: str) -> str:
    """
    Inverse of encoder()
    Convert base4 string to original string.

    Arg:
        string (str) - base4 string (lengh % 4 == 0).

    Return:
        converted (str) - original string.
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
    Create string of base4 number, which length is input.
    (forbidden = ["1001", "1021", "1101", "1200"] can't
     be found in cirtain string.)

    Arg:
        num (int) - lenght of string

    Return:
        filler (string)
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






### Encrypting Process

def completeter(username: str, password: str) -> tuple[str, str]:
    """
    Complete encoded username and password with start, stop and type codon.

    Args:
        username (str) - username
        password (str) - password

    Return:
        username_complete (str) - username with codons
        password_complete (str) - password with codons
    """

    username_complete = Codon_start + Codon_userp + encoder(username) + Codon_stopt
    password_complete = Codon_start + Codon_passw + encoder(password) + Codon_stopt

    return username_complete, password_complete




def encrypter(username: str, password: str) -> str:
    """
    Make encrypted string in base4 (length = 256) 
    that's contain encoded username and password.

    Args:
        username (str) - username
        password (str) - password

    Return:
        encrypted (str) - encrypted string in base4
    """


    # Encode inputs
    username2 , password2 = completeter(username, password)


    # Index logic
    max_length = 256
    username_lenght = len(username2)
    password_lenght = len(password2)

    start_username = random.randint(0, max_length - username_lenght)
    start_password = random.randint(0, max_length - password_lenght)


    while not (start_username + username_lenght <= start_password\
            or start_password + password_lenght <= start_password):

            start_password = random.randint(0, max_length - password_lenght)


    stop_username = start_username + username_lenght - 1
    stop_password = start_password + password_lenght - 1


    position_node = [start_username, stop_username, start_password, stop_password]
    position_node.sort()

    # Filler unit
    filler_first = filler_function(position_node[0])
    filler_mid = filler_function(position_node[2] - position_node[1])
    filler_last = filler_function(max_length - position_node[3])

    # Construct Outputs
    encrypted = filler_first + username2 + filler_mid + password2 + filler_last

    while len(encrypted) < 256:
        encrypted += "1"

    while len(encrypted) > 256:
        encrypted = encrypted[0: -1]
    

    return encrypted




def decrypter(encrypted: str) -> tuple[str, str]:
    """
    Inverse of encrypter()
    Find codons and extract original username and password form it.

    Arg:
        encrypted (str) - encrypted string in base4

    Return:
        username (str) - username
        password (str) - password
    """

    if encrypted == None:
        return None, None

    # Find all indices of start codons
    start_username_idx = encrypted.find(Codon_start + Codon_userp)
    start_password_idx = encrypted.find(Codon_start + Codon_passw)
    
    if start_username_idx == -1 or start_password_idx == -1:
        return None, None
    
    # Find stop codon locations
    stop_username_idx = encrypted.find(Codon_stopt, start_username_idx)
    stop_password_idx = encrypted.find(Codon_stopt, start_password_idx)
    
    if stop_username_idx == -1 or stop_password_idx == -1:
        return None, None
    
    # Extract the username and password
    username = decoder(encrypted[start_username_idx + len(Codon_start + Codon_userp):stop_username_idx])
    password = decoder(encrypted[start_password_idx + len(Codon_start + Codon_passw):stop_password_idx])
    
    return username, password




def encrypter_translation(encrypted: str) -> str:
    """
    Randomly select Pattern and format input to that pattern.
    (From A, T, C, G) Add key in front of string to indentify.

    Arg:
        encrypted (str) - base4 string.
    
    Return:
        encrypted_translated (str) - formated from of input.

    """

    encrypted_translated = encrypted

    seed_key = random.randint(0, 23)

    encrypted_translated = encrypted_translated.replace("0", Patern[seed_key][0])
    encrypted_translated = encrypted_translated.replace("1", Patern[seed_key][1])
    encrypted_translated = encrypted_translated.replace("2", Patern[seed_key][2])
    encrypted_translated = encrypted_translated.replace("3", Patern[seed_key][3])

    encrypted_translated = Key[seed_key] + encrypted_translated

    return encrypted_translated




def decrypter_translation(encrypted: str) -> str:
    """
    Inverse of encrypter_translation()
    Detect the key and convert back to base4 string.

    Arg:
        encrypted (str) - A, T, C, G format string.

    Return:
        translated (str) - original base4 string.

    """
    if encrypted == None:
        return None

    key_string = encrypted[:12]

    if key_string not in Key:
        return None

    seed_key = Key.index(key_string)

    translated = encrypted[12:]
    
    basic_A = str(Patern[seed_key].index("A"))
    basic_T = str(Patern[seed_key].index("T"))
    basic_C = str(Patern[seed_key].index("C"))
    basic_G = str(Patern[seed_key].index("G"))

    translated = translated.replace("A", basic_A)
    translated = translated.replace("T", basic_T)
    translated = translated.replace("C", basic_C)
    translated = translated.replace("G", basic_G)

    return translated






### Interfaces

def add_profile() -> tuple[str, str, str]:
    """
    Require user inputs username, password and usernote.
    
    Block:
        Blank inputs        (Only username, password)
        Surpass limit       (Only username, password)
        Invalid characters  (Only username, password)

    Return:
        username (str) - username
        password (str) - password
        usernote (str) - usernote
    """


    is_blank = False
    is_surpass = False
    is_invalid = False


    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
Add new profile

Only Upper/Lowercase, Base10 Integer, "." and "@" for Username and Password.
Maximum character length is 16 for Username and Password.
""")
    username = input("Username : ")
    password = input("Password : ")
    usernote = input("Usernote : ")
    # input("Enter to continue.")
    print()

    if len(username) == 0 or len(password) == 0:
        is_blank = True
    
    if len(username) > 16 or len(password) > 16:
        is_surpass = True

    for character in username:
        if character not in char_valid:
            is_invalid = True


    for character in password:
        if character not in char_valid:
            is_invalid = True



    if not (is_blank or is_surpass or is_invalid):
        return username, password, usernote
    
    else:
        print("-------------------------------------")
        if is_blank:
            print("Error: Blank")
        if is_surpass:
            print("Error: Surpass 16 characters")
        if is_invalid:
            print("Error: Invalid character(s)")
        
        print()

        input("Enter to continue.")
        
        return None, None, None




def del_profile(max_index: int):
    """
    Recive user delete index.

    Arg:
        max_index (int) - maximum index.
    
    Return:
        selected_index (int) - selected index to delete.
    or  None - when error occur.

    """

    print("Delete Profile")

    selected_index = input("Select index: ")
    # input("Enter to continue.")
    print()

    if selected_index == "":
        print("Error: Blank.")
        input("Enter to continue.")
        return None

    elif int(selected_index) in list(range(0, max_index)):
        return int(selected_index)

    else:
        print("Error: Index out of range.")
        input("Enter to continue.")
        return None
    



def red_profile(max_index: int):
    """
    Recive user read index.

    Arg:
        max_index (int) - maximum index.
    
    Return:
        selected_index (int) - selected index to read.
    or  None - when error occur.

    """

    print("Read Encrypted Code")

    selected_index = input("Select index: ")
    # input("Enter to continue.")
    print()

    if selected_index == "":
        print("Error: Blank.")
        input("Enter to continue.")
        return None

    elif int(selected_index) in list(range(0, max_index)):
        return int(selected_index)

    else:
        print("Error: Index out of range.")
        input("Enter to continue.")
        return None




def reg_profile() -> tuple[str, str]:
    """
    Recive user encrypted code and register.

    Return:
        unregister_code (str) - unregister code.
        usernote (str) - usernote.
    or  None - when error occur.

    """

    os.system('cls' if os.name == 'nt' else 'clear')

    print("""Register New Code

""")

    unregister_code = input("Unregistered Code : ")
    usernote = input("Usernote          : ")
    # input("Enter to continue")
    print()

    username, password = decrypter(decrypter_translation(unregister_code))

    if unregister_code == "":
        print("-------------------------------------")
        print("Error: Blank")
        print()
        input("Enter to continue.")
        return None, None
    
    elif username == None or password == None:
        print("-------------------------------------")
        print("Error: Invalid format")
        print()
        input("Enter to continue.")
        return None, None

    else:
        return unregister_code, usernote












all_profile = []
profile = []



while True:



    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"All Profiles ({len(all_profile)})")

    for index in range(len(all_profile)):
        print(f"""
Profile #{index}:
    {all_profile[index][0]}

Note:
    {all_profile[index][1]}

""")
    

    print("""

""")

    print("""
Console Command:
          (0)   Add Profile
          (1)   Del Profile
          (2)   Read Encrypted Code
          (3)   Register Encrypted Code
""")
    
    console = input("Console : ")




    if console == "0":
        username, password, usernote = add_profile()

        if username != None and password != None:
            profile = [encrypter_translation(encrypter(username, password)), usernote]
            all_profile.append(profile)

        profile = []




    elif console == "1":
        print("""

""")
        index = del_profile(len(all_profile))

        if index != None:
            if index == 0 and len(all_profile) == 1:
                all_profile = []
            else:
                all_profile.remove(all_profile[index])




    elif console == "2":
        print("""

""")
        if len(all_profile) == 0:
            print()
            print("Error: No profile")
            input("Enter to continue.")
            continue
        
        index = red_profile(len(all_profile))

        if index != None:
            username, password = decrypter(decrypter_translation(all_profile[index][0]))


            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"Read Profile #{index}")
            print(f"""
Profile #{index}:
    {all_profile[index][0]}

Note:
    {all_profile[index][1]}

Username:   {username}
Password:   {password}

""")
            input("Enter to continue.")
        

    

    elif console == "3":
        unregister_code, usernote = reg_profile()

        if not (unregister_code == None or usernote == None):
            profile = [unregister_code, usernote]
            all_profile.append(profile)


    else:
        print()
        print("Error: Invalid Command.")
        input("Enter to continue.")
        






"""
Type of Errors
    Invalid command
    No Profile
    Index out of range
    Invalid format
    Blank
    Surpass maximum characters
    Invalid Character

"""



















# End of Project