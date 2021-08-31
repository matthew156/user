class User:
    def __init__(self, name, email,) :
        self.name = name
        self.withdrawl = email
        self.money = 0
    def make_deposit(self, amount):
        self.money += amount
    def make_withdrawl(self, amount):
        self.money -= amount
    def display_user_balance(self):
        print(self.money)
    
person = User('Charles', 'charles@fakeemail.com') 
person2 = User('Hank', 'hank@fakeemail.com') 
person3 = User('Phil', 'phil@fakeemail.com') 

print(person.name)
person.make_deposit(100).person.make_deposit(200).person.make_deposit(300).person.display_user_balance().person2.make_deposit(200).person2.make_deposit(300).person2.make_withdrawl(100).person2.make_withdrawl(50).person2.display_user_balance().person3.make_withdrawl(400).person3.make_withdrawl(500).person3.make_deposit(1000).person3.make_withdrawl(50).person3.display_user_balance()