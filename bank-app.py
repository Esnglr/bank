import random

class Person:

    def __init__(self,name,surname,age,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

class card:

    def __init__(self,id,balance):
        self.id = id
        self.balance = balance

    def setId(self):
        id = random.randint(548959,59054805)
        self.id = id

    def getBalance(self):
        return self.balance
class Bank:

    def __init__(self,Person):
        self.Person = Person
        self.balance = 0
        self.dollar = 0
        self.bitcoin = 0  # kur oranı bu
        self.dog = 0
        self.etherum = 0
        self.debt = 0
        self.interest = 0
        self.wallet = 0  # ne kadar bitcoin var
        self.cards = []


    def create_card(self):
        c = card()
        c.setId()
        self.cards.append(c)

    def show_cards(self):
        return self.cards
    def history(self,money):
        f = open("expenses","a")
        text = f"You did cart curt {money} \n"
        f.write(text)
        f.close()

    def transfer_money(self,money,person):
        if not self.balance < money:
            self.withdraw_money(money)
            person.deposite(money)
            self.history(money)
        else:
            return f"You are needy, you have {self.balance}"

    def credits(self,money):
        self.interest = random.randint(50,200)
        self.balance += money
        self.debt += money + money*self.interest/100

    def show_debt(self):
        self.history()
        return self.debt

    def show_balance(self):
        return self.balance

    def deposite(self,money):
        #check int
        self.balance += money

    def withdraw_money(self,money):
        if not money < self.balance:
            self.balance -= money
            self.history(money)
        else:
            return f"You are needy, You have {self.balance}"

    #def check_sufficent(self):


    def buy_dollars(self,money,m_type):
        currency = random.randint(24,45)
        print("Dollar :",currency)

        if m_type == "tr":

            if not self.balance < money*currency:
                self.dollar += money/currency
                self.balance -= money

            else:
                return f"You are needy, You have {self.balance}"

        else:
            if not money*currency > self.balance:
                self.dollar += money
                self.balance -= money*currency
            else:
                return f"You are needy, You have {self.balance}"

    def show_dollars(self):
        return self.dollar

    def crypto_Info(self):
        self.bitcoin = random.randint(100,45000)
        self.etherum = random.randint(36,28000)
        self.dog = random.randint(1,1000000)

        return "B:",self.bitcoin, "E:",self.etherum,"D:",self.dog

    def buy_bitcoin(self,money):#money= tl

        if not self.balance < money:
            self.wallet += money / self.bitcoin
            self.balance -= money

        else:
            return f"You are needy, You have {self.balance}"

    def show_wallet(self):
        return self.wallet

    def getInfo(self):
        return self.Person.name, self.balance


