from datetime import datetime, timedelta

number_of_days = int(input("Enter number of days: "))

def calculate_future_date():
    
    future_date = datetime.now() + timedelta(days=number_of_days)
    
    formated_datetime = future_date.strftime("%Y-%m-%d")
    
    print("Future Date: ", formated_datetime)
    
calculate_future_date()
    