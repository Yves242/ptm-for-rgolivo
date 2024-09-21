
# Function that gets a parameter and accesses it
def greet(name):
    """This function takes a name as parameters and says hi to it."""
    print(f"Hello, {name}!")


# Function that gets two parameters and accesses it
def add_two_numbers(a, b):
    """This function takes two numbers as parameters."""
    sum = a+b
    print(f"{a} + {b} = {sum}.")


# Pwede rin marami, see?
def add_five_numbers(a, b, c, d, e):
    """This function takes five numbers as parameters."""
    sum = a+b+c+d+e
    print(f"{a} + {b} + {c} + {d} + {e} = {sum}.")
    

# eto naman, returns something.
def give_sum_of_two_numbers(a, b):
    '''This function returns the sum of two numbers. As NUMBER.'''
    sum = a+b
    return sum


# Call the greet function
greet("Alice")  # Output: Hello, Alice!

# Do the other things
add_two_numbers(1,2)
add_five_numbers(1,2,3,4,5)
give_sum_of_two_numbers(10,20)