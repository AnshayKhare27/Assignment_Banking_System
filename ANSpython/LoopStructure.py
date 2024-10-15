customers = int(input("Enter no. of customers:\n"))

for i in range(customers):
    initial_balance = int(input("Provide initial balance for customer\n"))
    annual_interest_rate = int(input("Provide annaul interest rate for customer\n"))
    years = int(input("Provide no. of years for customer\n"))

    future_balance = initial_balance * pow((1 + annual_interest_rate/100),years)
    print("Total future balance will be=> ",future_balance)


