import random

print("jag vill rulla en tärning")

try:
    sides = int(input("hur många sidor: "))
except:
    print ("tärningen behöver 1+ sidor")
    sides = 1
run = "y"

while run.lower() == "y":
    randomnumber = random.randint(1, sides)
    print(randomnumber)
    
    run = input("vill du rulla en till tärning y/n")





