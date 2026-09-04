agent_number = input("What is your agent number: ")
security_level = int(input("What is your security level: "))

if agent_number == "007" or security_level >= 5:
    print("ACCESS GRANTED")
elif security_level == 0:
    print("SECURITY ALERT! Nice try.")
else:
    print("ACCESS DENIED")