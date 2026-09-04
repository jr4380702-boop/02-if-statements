# write a program that asks for 3 inputs
# num1, num2, and an operator (+,-,/,*, or %)
# take the numbers, do math, and show the full expression.
# eg. if the input was 4, 5, and +, you print "4 + 9 = 9"
# if an invalid operator is given, report that it was invalid
# you will need variables, if, elif, else

num_one = int(input("input your first number: "))
num_two = int(input("input your second number: "))
operator = input("input one of these operators (+,-,/,*, or %): ")

if operator == "+":
    result = num_one + num_two
elif operator == "-":
    result = num_one - num_two
elif operator == "/":
    result = num_one / num_two
elif operator == "*":
    result = num_one * num_two
elif operator == "%":
    result = num_one % num_two
else:
    print("invalid operator")

print(f"{num_one} {operator} {num_two} = {result}")