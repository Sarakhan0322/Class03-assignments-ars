# Control Flow: if-else
age = 20
if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")

# if-elif-else
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# For loop
for i in range(5):
    print("Number:", i)

# While loop
x = 0
while x < 3:
    print("x is", x)
    x += 1

# Break & Continue
for i in range(5):
    if i == 3:
        break
    print("Before break:", i)

for i in range(5):
    if i == 2:
        continue
    print("Before continue:", i)
