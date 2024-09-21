# Create a list with some initial values
fruits = ["apple", "banana", "cherry"]

# Print the entire list
print("Original list:", fruits)

# Add a new item to the list
fruits.append("orange")
print("After adding 'orange':", fruits)

# Access an element by its index
print("The first fruit is:", fruits[0])

# Modify an element in the list
fruits[1] = "blueberry"
print("After changing the item with index 1 into 'blueberry':", fruits)

# Remove an item from the list
fruits.remove("cherry")
print("After removing 'cherry':", fruits)

# Iterate through the list and print each item
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)
