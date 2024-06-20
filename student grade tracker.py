 # input values
roll = int(input("Enter Roll: "))
name = input("Enter Name: ")
print("Enter marks of 5 subjects: ")
marks = []
for i in range(5):
    marks.append(int(input("Subject " + str(i + 1) + ": ")))

# Find total
total = 0
for x in marks:
    total += x

# Find percentage
per = total / 5

# Find Grade
if per >= 85:
    grade = "S"
elif per >= 75:
    grade = "A"
elif per >= 65:
    grade = "B"
elif per >= 55:
    grade = "C"
elif per >= 50:
    grade = "D"
else:
    grade = "F"

# Print all details
print("Roll Number:", roll)
print("Name:", name)
print("Marks:")
for x in marks:
    print(x)
print("Grade:", grade)
