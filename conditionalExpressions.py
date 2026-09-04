# Conditional Expressions are one-line shortcuts for if-else
score = 85
# conditional expression (sometimes called ternary):
# result = X if condition else Y
# condition: that"s the boolean expression
# Y the value if false
outcome = "passed" if score >= 70 else "failed"

print(f"With a score of {score}, you {outcome}")

num = 8
result = "spelt eight" if num >= 8 else "not spelt eight"# determine with a conditional expression whether it is even or odd
print(f"The number {num} is {result}")