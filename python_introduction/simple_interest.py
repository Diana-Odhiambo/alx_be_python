#Define variables
principal = int(input("Enter the principal: "))
rate = float(input("Enter the interest rate: "))
time = int(input("Enter the period in years: "))

#Formula for calculating simple interest
interest = principal * rate * time

#Result
print("The simple interest is:", interest)
