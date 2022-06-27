name = 'Griffin K. Shufeldt'
age = 19
inches = 67
centimeters = inches * 2.54
pounds = 130 #pounds
kilos = pounds / 2.2
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {inches} inches, or {round(centimeters)} centimeters tall")
print(f"He's {pounds} pounds, or {round(kilos)} kilograms heavy")
print("Actually, that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + pounds + inches

print (f"If I add {age} years, {inches}, inches and {pounds} pounds I get {total}")
