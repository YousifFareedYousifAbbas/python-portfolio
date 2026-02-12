# Week 1 – Strings Exercises

text = "Python Programming"

# First and last character
print("First character:", text[0])
print("Last character:", text[-1])

# Length of string
print("Length:", len(text))

# Uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Count occurrence of 'o'
count_o = 0
for letter in text:
    if letter == "o":
        count_o += 1
print("Number of 'o':", count_o)

# Reverse string
reversed_text = ""
for c in text:
    reversed_text = c + reversed_text
print("Reversed text:", reversed_text)
