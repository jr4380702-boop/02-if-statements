atk = int(input("What is your attack power: "))
defense = int(input("What is the monster's defence: "))
monster_health = int(input("what is the monster's health: "))
dmg = atk - defense
if dmg < 0:
    dmg = 0
if dmg > 50:
    print("CRITICAL HIT!")
elif dmg > 20:
    print("Solid hit!")
else:
    print("Weak hit.")
print(f"Your damage was {dmg} and the monster's hp is at {monster_health-dmg} now.")