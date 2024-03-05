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
waseem = BankAccount(0.01, 1000)
mahmoud = BankAccount(0.1, 200)
waseem.deposit(100).deposit(1000).deposit(500).withdraw(5000).yield_interest().display_account_info()
mahmoud.deposit(1000).withdraw(200).withdraw(500).withdraw(100).yield_interest().display_account_info()