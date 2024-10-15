def nestedCondition():
    print("*******************")
    print("*       ATM       *")
    print("*******************")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("*******************")

    balance = int(input("Enter your current balance: "))

    transaction = int(input("Press 2 to Withdraw or 3 to Deposit\n"))

    if(transaction==3):
        deposit_amt = int(input("How much amount would you like to Deposit\n"))
        if(deposit_amt<=0):
            print("Invalid amount")
            return
        
        balance += deposit_amt
        print("Amount deposited successfully!")

    elif(transaction==2):
        withdraw_amt = int(input("What amount would you like to Withdraw(should be in multiples 0f 100 or 500)\n")) 
        if(withdraw_amt<=0 or withdraw_amt>balance or (withdraw_amt%100!=0)):
            print("Invalid amount")
            return

        balance -= withdraw_amt
        print("Amount withdrawn successfully!")  

    else:
        print("Invalid entry")    


       

      