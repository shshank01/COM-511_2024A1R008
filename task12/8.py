# Write a menu-driven python program where the user can add items, remove items, view cart, and exit

cart = []
while True:
    print("1. Add items")
    print("2. Remove items")
    print("3. View cart")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter the item to add: ")
        cart.append(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        cart.remove(item)
    elif choice == "3":
        print("Cart: ", cart)
    elif choice == "4":
        break