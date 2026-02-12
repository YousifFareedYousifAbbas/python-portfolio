# Week 1 – Tuples Exercises

languages = ("Python", "Java", "C++", "JavaScript")

# Access first and last language
print("First language:", languages[0])
print("Last language:", languages[-1])

# Convert tuple to list to modify
languages_list = list(languages)
languages_list[3] = "Go"
print("Modified list:", languages_list)
