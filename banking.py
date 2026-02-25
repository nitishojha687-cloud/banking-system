customer = {}

def add_customer(c_account, name, balance):
    if c_account in customer:
        print("Account already exists!")
    else:
        customer[c_account] = {"name": name, "balance": balance}
        print("Account added successfully!")

def view_account():
    print("\n----- Account Details -----")
    if not customer:
        print("No accounts found.")
    else:
        for acc, info in customer.items():
            print(f"Account Number: {acc} | Name: {info['name']} | Balance: {info['balance']}")

def search_customer(c_account):
    print("\n----- Search Customer -----")
    if c_account not in customer:
        print("Customer account doesn't exist!")
    else:
        print(f"Name: {customer[c_account]['name']} | Balance: {customer[c_account]['balance']}")

def main():
    # Pre-added customers (only added once)
    add_customer(101, "John", 5000)
    add_customer(102, "Bob", 3000)
    add_customer(103, "Dalla", 8000)
    add_customer(104, "Deba", 2500)
    add_customer(105, "Rakesh", 10000)

    while True:
        print("\n1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            try:
                acc = int(input("Enter Account Number: "))
                name = input("Enter Name: ")
                balance = float(input("Enter Balance: "))
                add_customer(acc, name, balance)
            except ValueError:
                print("Invalid input! Account number and balance must be numbers.")

        elif choice == 2:
            view_account()

        elif choice == 3:
            try:
                acc = int(input("Enter Account Number to Search: "))
                search_customer(acc)
            except ValueError:
                print("Account number must be a number!")

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

main()