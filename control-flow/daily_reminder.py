while True:
    task = input("Enter your task: ")
    priority = input("Enter priority level (high, medium, low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if priority not in ["high", "medium", "low"]:
        print("Incorrect priority level. Please enter high, medium, or low.")
        continue

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a HIGH priority task. Please complete it as soon as possible.")

        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a MEDIUM priority task that should be completed soon (time-sensitive).")
            else:
                print(f"Reminder: '{task}' is a MEDIUM priority task. You can complete it at your own pace.")

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a LOW priority task but still time-sensitive. Try not to delay.")
            else:
                print(f"Reminder: '{task}' is a LOW priority task. Consider completing it in your free time.")

    break

