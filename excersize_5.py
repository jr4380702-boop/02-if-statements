tacos = int(input("How many tacos: "))
taco_price = float(input("What is the price of the tacos: "))
age = int(input("What is your age: "))
total = tacos*taco_price

if tacos >= 10 and age < 18:
    discount = total / 4
    discounted_total = total - discount
    print(f"your total was {total:.2f}, but now it is {discounted_total:.2f}.")
elif tacos >= 10 or age < 18:
    discount = total / 10
    discounted_total = total - discount
    print(f"your total was {total:.2f}, but now it is {discounted_total:.2f}.")
else:
    print(f"your total is {total:.2f}")