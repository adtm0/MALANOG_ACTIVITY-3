#Prompt user for purchase amount

amount = float(input("Enter purchase amount: "))

# Compute tax and round off to 2 decimal places

tax = (0.06 * amount).__round__(2)

# Display tax
print(f"Sales tax is", tax)