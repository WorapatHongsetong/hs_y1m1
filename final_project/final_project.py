"""
# Approved Lib
    # math
    # random
    # time
    # keyboard

# Clear Screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
"""


### Character Mapping
char_mapping = {}

# Mapping digits 0-9
for i in range(10):
    char_mapping[str(i)] = i

# Mapping letters a-z
for i, letter in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    char_mapping[letter] = 10 + i

# Mapping special characters '.' and '@'
char_mapping['.'] = 62
char_mapping['@'] = 63



