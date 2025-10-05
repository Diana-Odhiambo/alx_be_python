def safe_divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Division by zero not allowed")
    return (numerator / denominator)

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = safe_divide(num1, num2) 
    print("Result is", result)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a number")
    
