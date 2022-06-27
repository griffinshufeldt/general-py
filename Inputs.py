#Takes in user inputs
age = int(input("How old are you? "))
height = input("How tall are you? ")
weight = input("How much do you weigh? " )

#summarizes inputs
print(f"So, you're {age} years old, {height} tall and {weight} pounds heavy.")

#checks imputs
if age > 25:
    print ("you're old!")
else:
    print("You're young!")
    
if height > 180:
    print("You're tall!)
else if height >= 170 and <= 180:
     print("You're average height!)
else:
     print("You're short!)
    
