# Ask the user to enter a number
num = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True  

# A prime number is greater than 1
if num < 2:
    is_prime = False
else:
    # Check if the number is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:  # If it's divisible, it's not prime
            is_prime = False
            break  # Stop checking since we already found a factor

# Print the result
if is_prime:
    print(f"{num} is a prime number!")
else:
    print(f"{num} is NOT a prime number.")
