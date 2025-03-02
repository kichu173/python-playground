import os # os is a module in the Python Standard Library. It provides a way of using operating system dependent functionality.
from dotenv import load_dotenv, dotenv_values # load_dotenv is a function, dotenv_values is a dictionary

# load_dotenv() # This will load the .env file into the environment. The .env file should be in the same directory as the script.
#
# print(os.getenv('MY_SECRET_KEY')) # This will print the value of MY_SECRET_KEY from the environment
# print(os.getenv('COMBINED'))
# print(os.getenv('MAIL'))

# config = dotenv_values(".env") # This will load the .env file into a dictionary
# print(config)
# print(config['MY_SECRET_KEY']) # This will print the value of MY_SECRET_KEY from the dictionary

# print(os.environ)

config = {
    **dotenv_values(".env.shared"), # This will load the .env.shared file into a dictionary, ** is used to unpack the dictionary
    **dotenv_values(".env.secret")
}

print(config)

# pip install python-dotenv
# Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.
# This is useful for storing sensitive information, such as API keys, outside of your codebase.
# The .env file is a text file where each line is in the form of KEY=VALUE

"""
Advantages of using environment variables:
Scope: The environment variables are only available to the current Python process and its subprocesses.
Not System-Wide: They are not set as system-wide environment variables on your Windows machine.
Temporary: The environment variables are temporary and only exist for the duration of the Python process.
"""