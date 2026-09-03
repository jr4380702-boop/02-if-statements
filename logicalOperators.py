ontask = True
library_volume = True

# logical operators (And, Or, Not)
if ontask and library_volume:
    print("What a wonderful class!")
elif ontask or library_volume:
    print("This class is pretty good")
    if not ontask: # inverts a boolean value.  So true becomes false, and false becomes true
        print("Just get on task!")
    else:
        print("Shhhhhhhhhhhhh.  Just quiet down my beloved class.")
else:
    print("Is it 2:40 yet?!")