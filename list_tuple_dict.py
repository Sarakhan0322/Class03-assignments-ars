# Lists
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Fruits list:", fruits)
fruits.remove("banana")

# Accessing items
print("First fruit:", fruits[0])

# Tuples
colors = ("red", "green", "blue")
print("Colors:", colors)
print("Second color:", colors[1])

# Dictionaries
student = {
    "name": "Ali",
    "age": 22,
    "grade": "A"
}
print("Student name:", student["name"])
student["age"] = 23
student["major"] = "Computer Science"
print("Updated student info:", student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)
