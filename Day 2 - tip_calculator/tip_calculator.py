print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

pay = round(total * (1 + tip / 100) / people, 2)
pay = "{:.2f}".format(pay)

print(f"Each person should pay: ${pay}")
