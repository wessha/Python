class User:
    def __init__(self, address, name, email, balance = 0):
        self.address = address
        self.name = name
        self.email = email
        self.balance = balance
    def make_deposite(self,amount):
        self.balance += amount
        return(self)
    def make_withdrow(self, out):
        self.balance -= out
        return(self)
    def make_transfer(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            return(self)
        else :
            return 0

waseem = User("Ramallah", "waseem", "waseem@gmail.com")
mahmoud = User("Tulkarm", "Mahmoud", "mahmoud@gmail.com", 1000)
ahmed = User("Nablus", "Ahmed", "ahmed@gmail.com")
print(waseem.balance)
print(mahmoud.balance)
waseem.make_deposite(100).make_deposite(200).make_withdrow(100)
mahmoud.make_deposite(250).make_deposite(100).make_withdrow(73).make_withdrow(87)
ahmed.make_deposite(478).make_withdrow(99).make_withdrow(64).make_withdrow(90)
waseem.make_transfer(mahmoud,100)
print(waseem.balance)
print(mahmoud.balance)
print(ahmed.balance)