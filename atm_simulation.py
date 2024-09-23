import os

# Define the file where the account balance will be stored
balance_file = "balance.txt"

# Function to load the balance from the file or initialize it if not present
def load_balance():
    if not os.path.exists(balance_file):
        with open(balance_file, "w") as file:
            file.write("0")
        return 0
    else:
        with open(balance_file, "r") as file:
            return int(file.read())

# Function to save the balance to the file
def save_balance(balance):
    with open(balance_file, "w") as file:
        file.write(str(balance))

# Function to show the balance
def check_balance():
    balance = load_balance()
    print(f"Your current balance is: ₹{balance}")

# Function to deposit money
def deposit():
    balance = load_balance()
    amount = int(input("Enter the amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        save_balance(balance)
        print(f"₹{amount} deposited successfully!")
    else:
        print("Invalid amount. Try again.")

# Function to withdraw money
def withdraw():
    balance = load_balance()
    amount = int(input("Enter the amount to withdraw: ₹"))
    if amount > 0 and amount <= balance:
        balance -= amount
        save_balance(balance)
        print(f"₹{amount} withdrawn successfully!")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        print("Invalid amount. Try again.")

# Main function to display the ATM menu and handle user input
def atm_menu():
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Exiting. Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the ATM menu
if __name__ == "__main__":
    atm_menu()