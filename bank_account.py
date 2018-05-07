
class User:
    def __init__(self,first_name,last_name,middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

class Bank_Account:
    def __init__(self,user,account_type,balance):
        self.user = user
        self.account_type = account_type
        self.balance = balance
        

    def Open_Account(self):
        if(self.balance == 100):
            print("Account is created")
        else:
            print("You should have a minimum balance of $100")  

    def transfer(self,amount,to_account):
        to_account.balance += amount
        print(f"Amount {amount} is deposited into your account")
        return amount

    def withdraw(self,amount,from_account):
        if (from_account.balance == 0):
            print("Your account has 0 balance. $35 needto be paid")   
        else:
            from_account.balance -= amount
            print(f"Amount {amount} is withdrawn from your account")
            return amount

    #def accountcheck(self,check_acc):
     #   if (check_acc.balance == 0):
      #      print("Your account has 0 balance. $35 needto be paid")   

user = User('Suz','Dan','M')
checking_acc = Bank_Account(user,'Checking',100)

print(checking_acc.user.first_name)
print(checking_acc.user.last_name)
print(checking_acc.balance)

checking_acc.Open_Account()

savings_acc =Bank_Account(user,'Savings',0)
saving_amount = savings_acc.transfer(10,savings_acc)



checking_acc1 = Bank_Account(user,'Checking',50)
print(checking_acc1.balance)
checking_acc1.withdraw(50,checking_acc1)
print(checking_acc1.balance)

#checking_acc1.accountcheck('Checking')





