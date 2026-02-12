# Week 1 – Sets Exercises  

numbers = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates using set
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# Add and remove elements
unique_numbers.add(7)
unique_numbers.remove(2)
print("After adding 7 and removing 2:", unique_numbers)

# Print all numbers
print("Numbers in the set:")
for n in unique_numbers:
    print(n)
