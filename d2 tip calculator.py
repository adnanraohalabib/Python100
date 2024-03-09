print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? \n"))
people = int(input("How many people to split the bill? \n"))
percentage = float(input("What percentage tip would you like to give? 10, 12 or 15 ? \n"))
payment = (bill + bill*percentage/100) /people
print(f"Each person should pay: ${round(payment,2)}")
