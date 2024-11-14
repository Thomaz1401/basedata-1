# Este programa permite al usuario gestionar un carrito de compras, 
# permitiendo agregar, eliminar y visualizar artículos con sus precios y cantidades.

def display_menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

# Inicializar listas para artículos y precios
item_names = []
item_prices = []
item_quantities = []

while True:
    display_menu()
    choice = input("Please enter an action: ")

    if choice == '1':
        # Agregar un nuevo elemento
        item_name = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{item_name}'? "))
        item_quantity = int(input("How many would you like to add? "))

        item_names.append(item_name)
        item_prices.append(item_price)
        item_quantities.append(item_quantity)

        print(f"'{item_name}' has been added to the cart.")

    elif choice == '2':
        # Mostrar el contenido del carrito de compras
        print("\nThe contents of the shopping cart are:")
        for index, (name, price, quantity) in enumerate(zip(item_names, item_prices, item_quantities), start=1):
            total_price = price * quantity
            print(f"{index}. {name} - ${total_price:.2f} (x{quantity})")

    elif choice == '3':
        # Eliminar un artículo
        print("\nThe contents of the shopping cart are:")
        for index, name in enumerate(item_names, start=1):
            print(f"{index}. {name}")

        item_to_remove = int(input("Which item would you like to remove? ")) - 1

        if 0 <= item_to_remove < len(item_names):
            removed_item = item_names.pop(item_to_remove)
            item_prices.pop(item_to_remove)
            item_quantities.pop(item_to_remove)
            print(f"'{removed_item}' has been removed.")
        else:
            print("Sorry, that is not a valid item number.")

    elif choice == '4':
        # Calcular el total
        total = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    elif choice == '5':
        # Abandonar
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please select again.")
