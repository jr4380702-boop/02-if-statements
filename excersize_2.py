pizzas = int(input("How many pizzas do you have: "))
students = int(input("How many students are coming: "))
pizza_slices = pizzas * 8
pizza_slices_per_student = pizza_slices / students

print(f"We have {students} students and {pizza_slices} pizza slices.")

if pizza_slices_per_student >= 3:
    print("Pizza overload!")
elif pizza_slices_per_student >= 2:
    print("Perfect amount of pizza!")
else:
    print("We need more pizza!")