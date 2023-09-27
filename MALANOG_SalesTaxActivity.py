#Prompt user for purchase amount

amount = float(input("Enter purchase amount: "))

# Compute tax (6%) and round off to 2 decimal places

tax = (0.06 * amount).__round__(2)

# Display tax
print("Sales tax is", tax)
