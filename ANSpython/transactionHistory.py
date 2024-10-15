transactions = []
while True:
    print("Choose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View transaction history")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter the deposit amount: "))
        transactions.append(("Deposit", amount))
        print("Deposit successful!")
    elif choice == 2:
        amount = float(input("Enter the withdrawal amount: "))
        transactions.append(("Withdrawal", amount))
        print("Withdrawal successful!")
    elif choice == 3:
        print("Transaction History:")
        for transaction in transactions:
            print(transaction[0], transaction[1])
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")