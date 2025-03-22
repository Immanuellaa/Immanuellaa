# Creating a tuple and a list
fruits_tuple = ("apple", "banana", "cherry")
fruits_list = ["Beans", "guava", "berry"]

# Tuples are immutable
 
fruits_tuple.append(1)  # This will cause an error
  

# Lists are mutable
fruits_list.append(1)  # No error
print("Updated List:", fruits_list)  # Output: ['Beans', 'guava', 'berry', 1]

# Measuring iteration speed
fruits_tuple = tuple(range(1000000))  
fruits_list = list(range(1000000))     
# Timing tuple iteration
tuple_time = timeit.timeit('for x in fruits_tuple: pass', globals=globals(), number=10)

# Timing list iteration
list_time = timeit.timeit('for x in fruits_list: pass', globals=globals(), number=10)

print(f"Tuple iteration time: {tuple_time:.6f} seconds")
print(f"List iteration time: {list_time:.6f} seconds")

if tuple_time < list_time:
    print(" Tuples iterate faster!")
else:
    print(" Lists iterate faster!")


 