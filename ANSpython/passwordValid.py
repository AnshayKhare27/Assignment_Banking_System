password = input("Create a new password:\n")

if len(password)==8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password) :
    print("Password created successfully!")

else:
    print("Invalid password. Try again!")    
