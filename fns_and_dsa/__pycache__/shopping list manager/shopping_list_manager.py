def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #prompt for and add an item
            pass
        elif choice == '2':
            #prompt for and remove item
            pass
        elif choice == '3':
            #prompt for and view list
            pass
        elif choice == '4':
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again!")
    
if __name__ == "__main__":
    main()