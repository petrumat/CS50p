# Input 2 numbers and convert to float type
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

# Print ',' between each 3 digits (thousands, millions etc.)
print(f"{z:,}")

# Print only 2 decimals (automatically rounds the result)
print(f"{z:.2f}")

# Combine formatting
print(f"{z:,.2f}")