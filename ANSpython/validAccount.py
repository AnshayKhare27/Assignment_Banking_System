while True:
    acct_no = input("Enter your account number:\n")

    if acct_no.isdigit() and len(acct_no)==8:
        balance = int(input("Enter balance for your account:\n"))
        break

    else:
        print("Try again!")    

print("The total balance for the particular account is:", balance)