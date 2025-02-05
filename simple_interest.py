# Program calculates the simple interest on a given principal amount, interest rate,and time

principal = int(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = int(input("Enter period in years: "))

# Calculates simple interest earned on an investment over a period of time

simple_interest = principal * rate * time

# Printing the results

print("The simple interest is:", simple_interest)

