#This script calculates the future age of a person
current_age = int(input("How old are you?"))
current_year = int(input("What is the current year?"))
future_year = int(input("Enter a future year:"))

#Formula for calculating future age
future_age = current_age + (future_year - current_year)

#printing the results
print(f"In {future_year}, you will be {future_age} years old.")
