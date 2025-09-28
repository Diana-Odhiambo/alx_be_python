from datetime import datetime

def display_current_datetime():
    
    current_datetime = datetime.now()
    
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Current Date and Time:", formatted_datetime)
    
display_current_datetime()