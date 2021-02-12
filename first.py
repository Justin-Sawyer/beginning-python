"""
The following code is from the Executing Python Code lesson

def print_message(message):
    print(message)


print_message("Hello World!")


my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
"""
"""
The following code is from the pip3 lesson

pip3 is designed to be used with python3

from flask import Flask
# In terminal run python3 first.py
# Gives errot message "ModuleNotFoundError: No module named 'flask'"
# We haven't installed the module!

# In terminal type "pip3 install flask"
# In terminal run python3 first.py
# No error message, so flask installed ok

# In terminal run pip3 freeze
# Lists dependencies

# In terminal run pip3 freeze --local > requirements.txt
# Adds file called requirements.txt in which the dependencies are listed

# In terminal run pip3 uninstall flask
# Removes flask

# In terminal run pip3 install -r requirements.txt
# Installs from file

# In terminal run python3 first.py
# No error = flask installed ok

"""
