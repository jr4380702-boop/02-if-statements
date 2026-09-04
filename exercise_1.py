age = int(input("What is your age: "))
height = int(input("What is your height in inches: "))

print(f"So you are {age} years old and {height/12} feet and {height%12} inches.")

if age >= 12 and height >= 54:
    print("You may ride The Pythonator!")
elif age >= 12:
    print("You're old enough, but not tall enough.")
else:
    print("Sorry, you're not ready for The Pythonator.")