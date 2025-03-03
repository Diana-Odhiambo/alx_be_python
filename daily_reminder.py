while True:
    
   task = input("Enter your task: ")
   priority = input("Enter priority level (high, medium, low): ").lower()
   time_bound = input("Is it time-bound? (yes/no): ").lower()

   if priority not in ["high", "medium", "low"]:
       print("incorrect priority level. Please enter high, medium, or low.")
       continue

   match priority:
     case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("Please complete the task soonest possible.")

     case "medium":
        print(f" '{task}' has a medium priority. You can complete it at your own time.")

     case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it at your own free time.")

   break
