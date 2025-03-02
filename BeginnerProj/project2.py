# Random Password generator
# Sometime while setting up a password, there's a few kind of sets of criteria that you need to fulfill - ex: it may need to be a certain length.
# So we want to ask the user what length the password should be. It may contain special characters or uppercase characters or things like numbers.

# Plan (call the function and test it, don't like to write too much code without testing functionality)
# 1. Collect user preferences
#    - length
#    - should contain upper case characters
#    - should contain special characters
#    - should contain numbers or digits

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string # gives us access to a list of all the characters that are lowercase, uppercase, digits, or special characters.

def generate_password():
    # Collect user preferences
    try:
        length = int(input("Enter the desired password length: ").strip())
    except ValueError as e:
        print("Try Again!!! Invalid input. Please enter a number.\n", e)
        return
    include_uppercase = input("Include uppercase characters? (y/n): ").strip().lower()
    include_special = input("Include special characters? (y/n): ").strip().lower()
    include_digits = input("Include digits or numbers? (y/n): ").strip().lower()

    # ensure length is valid
    if length < 4:
        print("Password length must be at least 4 characters.")
        return # you are going to exit the function and go back to the line they called the function from.

    # get all available characters
    lower = string.ascii_lowercase # gives all of the lowercase letters
    upper = string.ascii_uppercase if include_uppercase == 'y' else '' # inline IF statement or a Ternary statement. If the condition is true, then the first value is returned. If the condition is false, then the second value is returned.
    special = string.punctuation if include_special == 'y' else ''
    digits = string.digits if include_digits == 'y' else ''

    # print(type(upper), "type of upper") # <class 'str'> type of upper

    all_characters = lower + upper + special + digits

    # print(all_characters)

    # randomly pick characters up to the length
    # ensure we have at least one of each character type
    required_characters = [] # create an empty list
    if include_uppercase == 'y':
        required_characters.append(random.choice(upper)) # pick a one random character from the uppercase list and append it to the required_characters list
    if include_special == 'y':
        required_characters.append(random.choice(special))
    if include_digits == 'y':
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters + random.sample(all_characters, remaining_length) # random.sample() function returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set. Used for random sampling without replacement.

    random.shuffle(password)

    print(password)

    # convert list to a string
    str_password = ''.join(password) # join takes parameter as a list, all of the characters in the list together with no spaces in between them.
    return str_password


password = generate_password()
print(password)
