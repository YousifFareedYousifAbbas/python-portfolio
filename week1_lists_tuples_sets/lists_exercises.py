# Week 1 – Lists Exercises

fruits = ["apple", "banana", "orange", "grape", "watermelon"]

# Access first and last fruit
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add a new fruit
fruits.append("kiwi")
print("After adding kiwi:", fruits)

# Remove the second fruit
fruits.pop(1)
print("After removing second fruit:", fruits)

# Print fruits with length > 5
print("Fruits with more than 5 letters:")
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)
