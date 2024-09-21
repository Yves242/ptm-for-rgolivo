def fibonacci_while(n):
    # Initialize the first two Fibonacci numbers
    first_number = 0
    second_number = 1
    
    # Create an empty list to store the Fibonacci sequence
    fibonacci_sequence = []
    
    # Initialize a counter to keep track of how many numbers we have generated
    count = 0
    
    # Use a while-loop to generate the Fibonacci sequence
    while count < n:
        
        # Add the current Fibonacci number to the list
        fibonacci_sequence.append(first_number)
        
        # Update the Fibonacci numbers for the next iteration
        next_number = first_number + second_number 
        first_number = second_number 
        second_number = next_number
        
        # Increase the count of numbers generated
        count += 1
    
    # Print the entire Fibonacci sequence as a string, with numbers separated by spaces
    print(" ".join(map(str, fibonacci_sequence)))

# Ask the user to input a positive integer
n = int(input("Enter a positive integer: "))
fibonacci_while(n) 
