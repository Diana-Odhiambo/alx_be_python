def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            items = input("Enter items to add(separate with comas): ")
            items_list = items.split(",")
            
            for item in items_list:
                item = item.strip()
                if item:
                    shopping_list.append(item)
            print("Items added to the list")
            
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list!")
            else:
                print(f"'{item}' not found in shopping list.")
                
        elif choice == '3':
            if shopping_list:
                print("\nShopping List: ")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is empty")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            
if __name__ == "__main__":
    main()
            