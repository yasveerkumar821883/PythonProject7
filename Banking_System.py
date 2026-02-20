print("Welcome To ABC Bank 🏦 ")
def balance():
    print("Your balance : ")
def debit():
    print("Amount Debit : ")
def credit():
    print("Amount Credit : ")
def check_submit():
    print("Submit Check : ")
def create_account(mob_no,name,address):
    print("your account is open ")

    print(f"""
    Name :{name}
Mob_no :{mob_no}
Address :{address}""")
print("""1. New User 
2. Existing User 
3. Exit Thanks for Coming """)
while True:
    option1=input("Enter the Choice : ")
    if option1=="1":
        mob_no = input("Enter Mobile No: ")
        name = input("Enter the name : ")
        address = input("Enter the address :")
        create_account(mob_no,name, address)
        break
    elif option1=="2":
        print("Welcome to In your Account  : ")
        print("""1. Check Balance 
        2. Debit Money
        3. Credit  Money 
        4. Submit Check 
        5. Quit """)
        while True:
            option=input("Enter the Choice : ")
            if option=="1":
                balance()
            elif option=="2":
                debit()
            elif option=="3":
                credit()
            elif option=="4":
                check_submit()
            elif option=="5":
                print("Close the App!")
                break
            else:
                print("You Choose the Wrong Option ")
        break