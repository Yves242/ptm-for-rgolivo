# Define a string
my_string = "Hello, World!"

# (!important!) Accessing characters
first_char = my_string[0]   # 'H'
last_char = my_string[-1]   # '!'

# (!important!) Slicing strings
substring = my_string[7:12] # 'World'

# (!important!) String concatenation
new_string = my_string + " How are you?"  # 'Hello, World! How are you?'

# Repeating strings
repeated_string = "Ha! " * 3 # 'Ha! Ha! Ha! '

# (!important!) Changing case
uppercase_string = my_string.upper() # 'HELLO, WORLD!'
lowercase_string = my_string.lower() # 'hello, world!'

# Replacing substrings
replaced_string = my_string.replace("World", "Python") # 'Hello, Python!'

# Splitting strings
words = my_string.split(' ')  # ['Hello,', 'World!']

# Getting the length of the string
length_of_string = len(my_string)  # 13

# Output results
print(f"Original string: {my_string}")
print(f"First character: {first_char}")
print(f"Last character: {last_char}")
print(f"Substring from index 7 to 12: {substring}")
print(f"Concatenated string: {new_string}")
print(f"Repeated string: {repeated_string}")
print(f"Uppercase string: {uppercase_string}")
print(f"Lowercase string: {lowercase_string}")
print(f"Replaced string: {replaced_string}")
print(f"Split words: {words}")
print(f"Length of the string: {length_of_string}")
