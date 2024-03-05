class BankAccount:
	def __init__(self, int_rate = 0.01, balance = 0): 
		self.int_rate = int_rate
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
		return(self)
	def withdraw(self, amount):
		if amount >= self.balance:
			self.balance -= amount
		else:
			self.balance -= 5
			print("Insufficient funds: Charging a $5 fee")
		return(self)
	def display_account_info(self):
		print(f"Balance: ${self.balance}")
	def yield_interest(self):
		if self.balance > 0 :
			self.balance += self.balance * self.int_rate
		return(self)
class User:
    def __init__(self, address, name, email, balance = 0):
        self.address = address
        self.name = name
        self.email = email
        self.balance = balance
        self.account = BankAccount()
    def make_deposite(self):
        self.account.deposit
        return(self)
    def make_withdrow(self):
        self.account.withdraw
        return(self)
    def make_transfer(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            return(self)
        else :
            return 0
    def display_user_balance(self):
            self.account.display_account_info()
            print(self.name)
            return(self)
waseem = User("Ramallah", "waseem", "waseem@gmail.com")
mahmoud = User("Tulkarm", "Mahmoud", "mahmoud@gmail.com", 1000)
ahmed = User("Nablus", "Ahmed", "ahmed@gmail.com")

waseem.account.deposit(100).withdraw(50).display_account_info()