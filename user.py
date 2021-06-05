class User:
    bank_name="First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdraw(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.name, self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance-=amount
        other_user.account_balance+=amount

jojo=User('Jojo', 'jojo@jo.jo')
jojo.make_deposit(100)
jojo.make_deposit(50)
jojo.make_deposit(20)
jojo.make_withdraw(45)
jojo.display_user_balance()

rick=User('Rick', 'rick@roll.com')
rick.make_deposit(5000)
rick.make_deposit(2500)
rick.make_withdraw(6000)
rick.make_withdraw(1000)
rick.display_user_balance()

jim=User('Jim', 'jim@jimminy.ca')
jim.make_deposit(10000)
jim.make_withdraw(100)
jim.make_withdraw(1000)
jim.make_withdraw(20)
jim.display_user_balance()

jojo.transfer_money(jim, 75)
jojo.display_user_balance()
jim.display_user_balance()