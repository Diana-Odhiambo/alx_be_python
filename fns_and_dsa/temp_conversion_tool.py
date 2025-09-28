FAHRENEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENEIT_FACTOR = 9/5

try:
    temp = float(input("Enter the temparature to convert: "))
except ValueError:
      print("Invalid temparature! Please enter a numeric value.")
      exit()
      
temp_type = input("Is the temperature celsius or fahreneit? (C / F ): ").strip().upper()


def convert_to_celsius(fahreneit):
    return (fahreneit -32) * FAHRENEIT_TO_CELSIUS_FACTOR

def convert_to_fahreneit(celsius):
    return (celsius * CELSIUS_TO_FAHRENEIT_FACTOR) + 32

if temp_type == "C":
    print(f"{temp}°C is equal to {convert_to_fahreneit(temp):.2f}°F")
    
elif temp_type == "F":
    print(f"{temp}°F is equal to {convert_to_celsius(temp):.2f}°C")
    
else:
    print("Invalid temparature type! Please Enter 'C' or 'F'.")
