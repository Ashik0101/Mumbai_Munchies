class SnackInventory:
    def __init__(self):
        self.inventory = []

    def add_snack(self, snack_id, name, price, availability):
        snack = {'id': snack_id, 'name': name,
                 'price': price, 'availability': availability}
        self.inventory.append(snack)

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack['id'] == snack_id:
                self.inventory.remove(snack)
                print("Snack removed from the inventory.🙌🙌")
                break
        else:
            print("Snack not found in inventory.😒")

    def update_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack['id'] == snack_id:
                snack['availability'] = availability
                print("Snack availability updated.😎✌️")
                break
        else:
            print("Snack not found in inventory.😒")


class SalesRecords:
    def __init__(self):
        self.sales = []

    def record_sale(self, snack_id, snack_inventory):
        for snack in snack_inventory.inventory:
            if snack['id'] == snack_id:
                if snack['availability'] == 'yes':
                    snack['availability'] = 'no'
                    self.sales.append(snack)
                    print("Sale recorded.✌️✌️")
                    break
                else:
                    print("Snack is not available for sale.😒")
                    break
        else:
            print("Snack not found in inventory.😢")


snack_inventory = SnackInventory()
sales_records = SalesRecords()


def display_menu():
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update the availability of a snack")
    print("4. Record a sale")
    print("5. Exit")


def get_input(message):
    return input(message)


def add_snack_to_inventory():
    snack_id = get_input("Enter snack ID: ")
    name = get_input("Enter snack name: ")
    price = get_input("Enter snack price: ")
    availability = get_input("Enter snack availability (yes/no): ")
    snack_inventory.add_snack(snack_id, name, price, availability)
    print("Snack added to the inventory. 😎✌️")
    print()


def remove_snack_from_inventory():
    snack_id = get_input("Enter snack ID: ")
    snack_inventory.remove_snack(snack_id)


def update_snack_availability():
    snack_id = get_input("Enter snack ID: ")
    availability = get_input("Enter snack availability (yes/no): ")
    snack_inventory.update_availability(snack_id, availability)


def record_sale():
    snack_id = get_input("Enter snack ID: ")
    sales_records.record_sale(snack_id, snack_inventory)


while True:
    display_menu()
    choice = get_input("Enter your choice: ")

    if choice == '1':
        add_snack_to_inventory()
    elif choice == '2':
        remove_snack_from_inventory()
    elif choice == '3':
        update_snack_availability()
    elif choice == '4':
        record_sale()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
