credit_score = int(input("Enter your credit score: "))
annual_income = int(input("Enter your annual income: "))

if(credit_score>700 and annual_income>=50000):
    print("You are eligible for loan")

else:
    print("You are not eligible for loan")
