class bank_account():
	def __init__(self,acc_no,name,acc_type,balance=0):
		self.acc_no=acc_no
		self.name=name
		self.acc_type=acc_type
		self.balance=balance
		
	def deposit(self,amount):
		self.balance+=amount
		print(f"Deposited {amount}. New balance: {self.balance}")
					
		
	def withdraw(self,amount):
		if(amount<0):
			print("Insufficient funds")
		else:
			self.balance-=amount
			print(f"Withdrew {amount}. New balance: {self.balance}\n")
		

a1=bank_account("111","Athul","Savings",1000)
a1.deposit(400)
a1.withdraw(100)


a2=bank_account("112","Stephen","Savings",3000)
a2.deposit(4000)
a2.withdraw(1000)
