age = int(input("Enter Your Age: "))

# if
# Boolean expression (a comparison - something that resolves to True or False)
# don't forget the :
# >= (greater than or equal to) : comparison operator
# other basic comparison operators: == (equal), != (not equal), > (greater than), < (less than), <= (less than or equal to), >= (greater than or equal to)
# common mistake: using just one "=" for comparison ...don't do that, it is an assignment
if age >= 18:
    # notice the indent - anything intented is within this if statement
    print("Go enjoy your movie!")
elif age > 18: # short for else if
    print("Get in there you old man!")
elif age > 100:
    print("You're too old to be out this late.")
else: # this only executes if the other if and elif statements were false
    print("You're too young for this movie, go away.")