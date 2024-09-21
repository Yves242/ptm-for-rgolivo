# Define a dictionary with different types of keys
my_dict = {
    'name': 'Alice',          # String key
    1: 'one',                 # Integer key
    3.14: 'pi',               # Float key
    True: 'boolean_key'       # Boolean key
}

# Get the length of the dictionary
length_of_dict = len(my_dict)  # 4

# Accessing values
name_value = my_dict['name']          # 'Alice'
one_value = my_dict[1]                # 'one'
pi_value = my_dict[3.14]              # 'pi'
boolean_key_value = my_dict[True]     # 'boolean_key'

# Modifying values
my_dict[1] = 'updated_one'            # Updates value for key 1

# Adding new key-value pairs
my_dict[42] = 'answer'                # Adds a new key-value pair

# Removing key-value pairs
removed_value = my_dict.pop(3.14)     # Removes key 3.14 and returns 'pi'
del my_dict[True]                     # Removes key True

# Getting all keys and values
keys = my_dict.keys()                 # dict_keys(['name', 1, 42])
values = my_dict.values()             # dict_values(['Alice', 'updated_one', 'answer'])

# Output results
print(f"Original dictionary: {my_dict}")
print(f"Length of the dictionary: {length_of_dict}")
print(f"Name value: {name_value}")
print(f"Value for key 1: {one_value}")
print(f"Value for key 3.14: {pi_value}")
print(f"Value for key True: {boolean_key_value}")
print(f"Dictionary after modifications: {my_dict}")
print(f"Removed value for key 3.14: {removed_value}")
print(f"All keys: {list(keys)}")
print(f"All values: {list(values)}")
