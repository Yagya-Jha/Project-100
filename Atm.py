class ATM(object):
    def __init__(self, ATM_Card_Number, Pin_Number, Name):
        self.ATM_Card_Number = ATM_Card_Number
        self.Pin_Number = Pin_Number
        self.Name = Name
        self.balance = 0

    def add_money(self, money_to_add):
            self.balance += abs(money_to_add)
            print('\n')
            print('₹', abs(money_to_add), ' Added To Your Account')
            print('\n')

    def withraw_money(self, money_to_withdraw):
        if money_to_withdraw < self.balance:
            self.balance -= money_to_withdraw
            print('\n')
            print('₹', money_to_withdraw, ' Withdrawn From Your Account')
            print('\n')
        else:
            print('\n')
            print("You Don't Have Enough Money In Your Account")
            print('\n')

    def show_accont_details(self, show_confedential_information):
        print('\n')
        print('Account Holder Name:- ', self.Name)
        print('Available Bank Account Balance:- ', self.balance)
        if(show_confedential_information == True):
            print('ATM Card Number:- ', self.ATM_Card_Number)
            print('Pin Number:- ', self.Pin_Number)
            print('\n')
        else:
            print('\n')

name = input('Enter Your Name:- ')
atm_cnum = input('Enter Your Credit Card Number:- ')
atm_pnum = input('Enter Your Pin Number:- ')

atm = ATM(atm_cnum, atm_pnum, name)

print('Your Account is Successfully Registered !!')

print('________________________________________________________________________________________________________________')

quit = False

while quit == False:
    print('Would You Like to do Any Of the following?')
    print('=> Withraw Money')
    print('=> Add Money To Account')
    print('=> Show Account Details')

    what_to_do = str(input("(W, A, S) Respectively.'Q' To quit: "))
    whattodo = what_to_do.upper()
    if whattodo == 'W':
        money_to_withdraw = int(input('How Much Money You Want To Withraw? '))
        atm.withraw_money(money_to_withdraw)
    elif whattodo == 'A':
        money_to_add = int(input('How Much Money You Want To Add In you Account? '))
        atm.add_money(money_to_add)
    elif whattodo == 'S':
        s_c = str(input('Would You Like To See Confedential Details As Well? (y/n): '))
        if(s_c.upper() == 'Y'):
            atm.show_accont_details(True)
        elif(s_c.upper() == 'N'):
            atm.show_accont_details(False)

    elif whattodo == 'Q':
        quit = True