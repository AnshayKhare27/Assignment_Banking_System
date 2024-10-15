class Customer:
    def __init__(self, first_name, last_name, dob, email, phone_number, address):
        
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def print_info(self):
        print(f"Name: {self.get_full_name()}, Email: {self.email}, Phone: {self.phone_number}, Address: {self.address}")
