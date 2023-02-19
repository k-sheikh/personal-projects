#========LIBRARIES========

from tabulate import tabulate


#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return self.country, self.code, self.product, self.cost, self.quantity


#=============Shoe list===========

shoe_list = []


#==========Functions outside the class==============

# Read data from 'inventory.txt' file
def read_shoes_data():

    with open("inventory.txt", "r", encoding = "utf-8") as f:
        
        # Skip the first i
        next(f)
        
        # Perform operations on the rest of the file
        for i in f:
            i = i.strip().split(",")
            shoe_list.append(Shoe(i[0], i[1], i[2], int(i[3]), int(i[4])).__str__())

read_shoes_data()


# Capture data for new shoes
def capture_shoes():

    # User input
    country = input("\nPlease enter the product country: ")

    code = input("Please enter the product code: ")
    # Check if product code exists
    while any(code in sublist for sublist in shoe_list):
        print("Sorry, this code already exists.")
        code = input("Please enter the product code: ")
    
    product = input("Please enter the product name: ")
    # Check if product name exists
    while any(product in sublist for sublist in shoe_list):
        print("Sorry, this product already exists.")
        product = input("Please enter the product name: ")

    # Check if cost is an integer    
    while True:
        try:
            cost = int(input("Please enter the product cost: "))
            pass
        except ValueError:
            print("\nSorry. That is not a valid input.")
            continue
        else:
            break

    # Check if quantity is an integer
    while True:
        try:
            quantity = int(input("Please enter the product quantity: "))
            pass
        except ValueError:
            print("\nSorry. That is not a valid input.")
            continue
        else:
            break
    
    # Append to shoe list
    shoe_list.append(Shoe(country, code, product, cost, quantity).__str__())

    # Append shoe to 'inventory.txt' file
    with open ("inventory.txt", "a", encoding = "utf-8") as f:
        f.write(f"\n{country},{code},{product},{cost},{quantity}")

    # Print confirmation
    print("\nProduct has been added successfully.")


# View all shoe data in a table
def view_all():

    # Initialise header and print table using tabulate
    header = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate(shoe_list, headers = header, tablefmt = 'fancy_grid'))


# Update existing stock
def re_stock():

    # Find shoe with the lowest stock
    for i in shoe_list:
        search_code_list = min(shoe_list, key = lambda x: x[4])
    print(f"""\nThe following item is low on quantity:\n
Country:\t{search_code_list[0]}
Code:\t\t{search_code_list[1]}
Product:\t{search_code_list[2]}
Cost:\t\t{search_code_list[3]}
Quantity:\t{search_code_list[4]}""")

    restock_menu = input("\nWould you like to update the stock? (Yes/No): ").lower()

    while restock_menu not in ["yes", "no"]:
        print("\nSorry. That is not a valid input.")
        restock_menu = input("\nWould you like to update the stock? (Yes/No): ").lower()

    if restock_menu == "yes":
        while True:
            try:
                restock_quantity = int(input("\nEnter the quantity you would like to add:  "))
                confirm_restock = input(f"\nYou have added {restock_quantity} items, please confirm. (Yes/No): ").lower()
                while confirm_restock not in ["yes", "no"]:
                    print("\nSorry. That is not a valid input.")
                    confirm_restock = input(f"\nYou have added {restock_quantity} items, please confirm. (Yes/No): ").lower()

                if confirm_restock == "yes":
                    # Remove object from list
                    shoe_list.remove(search_code_list)
                    # Update and add new object to list
                    shoe_list.append(Shoe(search_code_list[0], search_code_list[1], search_code_list[2], search_code_list[3], (search_code_list[4] + restock_quantity)).__str__())
                    print("\nStock updated successfully.")

                    # Replace old quantity with new quantity
                    with open ("inventory.txt", "r", encoding = "utf-8") as f:
                        # Read entire file contents
                        data = f.read()
                        # Search and replace
                        data = data.replace(str(search_code_list[4]), str(search_code_list[4] + restock_quantity))

                    # Write replaced data
                    with open ("inventory.txt", "w", encoding = "utf-8") as f:
                        f.write(data)

                else:
                    print("\nStock not updated.")
                    pass

            except ValueError:
                print("\nSorry. That is not a valid input.")
                continue

            else:
                break

    elif restock_menu == "no":
        print("\nStock not updated.")
        pass


# Search for a shoe by the product code
def seach_shoe():

    search_code_list = []

    search_code = input("\nEnter the SKU code: ")

    for i in shoe_list:
        if i[1] == search_code:
            search_code_list.append(i)

    if len(search_code_list) > 0:
        print(f"""
Country:\t{search_code_list[0][0]}
Code:\t\t{search_code_list[0][1]}
Product:\t{search_code_list[0][2]}
Cost:\t\t{search_code_list[0][3]}
Quantity:\t{search_code_list[0][4]}""")

    else:
        print("\nCode not found.")


# Show total value of stock in a table
def value_per_item():

    shoe_list_value = []

    for i in shoe_list:
        shoe_list_value.append([i[0], i[1], i[2], int(i[3]), int(i[4]), int(i[3] * i[4])])

    header = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]
    print("")
    print(tabulate(shoe_list_value, headers = header, tablefmt = 'fancy_grid'))


# Show item marked for sale
def highest_qty():

    # Find shoe with the highest stock
    for i in shoe_list:
        search_code_list = max(shoe_list, key = lambda x: x[4])
    print(f"""\nThe following item should be marked for sale:\n
Country:\t{search_code_list[0]}
Code:\t\t{search_code_list[1]}
Product:\t{search_code_list[2]}
Cost:\t\t{search_code_list[3]}
Quantity:\t{search_code_list[4]}""")


# Logic for menu
def menu():
    
    menu = input('''\nPlease select one of the following options:
c\t- Capture shoe data
v\t- View all shoes
r\t- Restock
s\t- Search shoe
t\t- Total value per item
m\t- Mark item for sale
e\t- Exit
: ''').lower()

    if menu == "c":
        capture_shoes()

    elif menu == "v":
        view_all()

    elif menu == "r":
        re_stock()

    elif menu == "s":
        seach_shoe()

    elif menu == "t":
        value_per_item()

    elif menu == "m":
        highest_qty()

    # Exit program
    elif menu == "e":
        print(f"\nGoodbye!")
        exit()

    # Logic for accidental input
    else:
        print("\nYou have made a wrong choice. Please try again.")


#==========Main Menu=============

while True:
    
    menu()