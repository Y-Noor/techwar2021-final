acc_dict = {}
card_dict = {}
current_user = None
class Account:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.balance = 0
        self.accid = self.id_gen()
        self.cards = [self.id_gen()]
        self.state = True
        self.history = {self.cards[0] : []}

    def id_gen(self):
        import random
        string = self.fname[0] + self.lname[0]
        for i in range(0,9):
            string += str(random.randint(0,9))
        return string

    def gen_card(self):
        self.cards.append(self.id_gen())

    def debit(self, card_id, amt):
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        self.history[card_id].append(now + '--' + 'd' + str(amt))
        self.balance = self.balance + amt

    def credit(self, card_id, amt):
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        self.history[card_id].append(now + '--' + 'c' + str(amt))
        self.balance = self.balance - amt

    def check(self):
        return f"Current balance: {self.balance}"

def create_acc():
    fname = input("Please enter your firstname: ")
    lname = input("Please input your last name: ")
    print()
    temp_acc = Account(fname, lname)
    temp_acc.gen_card()

    print("Account created successfully")
    print("Your account ID :  ", temp_acc.accid)
    print("Your card ID    :  ", temp_acc.cards[0])
    acc_dict[temp_acc.accid] = temp_acc
    card_dict[temp_acc.cards[0]] = temp_acc
    print()

    main()


def login():
    print("Please choose an option\n1. Card ID\n2. Account ID")
    choice = eval(input("Enter your choice: "))
    print()
    if choice == 1:
        card()
    elif choice == 2:
        account()

def card():
    global current_user
    card_id = input("Enter the card ID:")
    if card_id in card_dict:
        print("Login  Successful")
        current_user = card_dict[card_id]
    else:
        print("Error")
    card_menu()

def account():
    global current_user
    account_id = input("Enter the account ID:")
    if account_id in acc_dict:
        current_user = acc_dict[account_id]
        card_menu()
    else:
        print("Error")

def card_menu():
    print("Please choose an option\n1. Credit Account\n2. Debit Account\n 3.view card information \n4.Disactivate card")
    choice = eval(input("Enter your choice: "))
    if choice == 1:
        x = int(input("Input amount to credit: "))
        credit_Acc(x)
    elif choice == 2:
        x = int(input("Input amount to debit: "))
        debit_Acc(x)
    elif choice == 3:
        view_info()
    elif choice == 4:
        disactivate_Card()

def credit_Acc(x):
    current_user.credit(current_user.cards[0], x)
    print(current_user.check())

def debit_Acc(x):
    current_user.debit(current_user.cards[0], x)
    print(current_user.check())

def view_info():
    print(current_user.check())


def disactivate_Card():
    pass

def main():
    while True:
        print("Please choose an option\n1. Create account\n2. Log in to account")
        choice = eval(input("Enter your choice: "))
        print()
        if choice == 1:
            create_acc()
        elif choice == 2:
            login()


main()
