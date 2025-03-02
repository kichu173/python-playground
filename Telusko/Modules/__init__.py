# __init__.py simply initialize the package by running some code whenever it's imported.
# This file is optional, but it's a good practice to have it in place in case you're planning to expand the package later on.

# utils (package)
# | -- string_util.py
# | -- math_util.py
# | -- __init__.py
# another package or root python file (main.py) - from utils.string_util import find_index, from utils.math_util import find_sqrt
print("imported pack") # https://www.youtube.com/watch?v=VEbuZox5qC4

# You can simplify the imports of different components or dependencies in your package with __init__.py

# from math_util import find_sqrt, from string_util import find_index - __init__.py
# main.py -- from utils import find_sqrt, find_index