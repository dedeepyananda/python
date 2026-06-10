"""
while True:
    account=100000
    password=1234
    card=input("insert card")
    print("card inserted")
    if card=="c":
        name=input("enter name:")
        print(f"Welcome {name}")
        a=int(input("enter password"))
        if a==1234:
            print("enter your choice\n 1.Balance Enquiery: \n 2.Withdraw Amount: \n")
            choice=int(input())
            if choice==1:
                print(f"Balance in your account is{account}")
                break
            elif  choice==2:
                print("enter amount to withdraw")
                b=int(input())
                if b>10000:
                    print("Insufficient funds")
                else:
                    c=account-b
                    print(f"amount with drawn successfully {b}")
                    c=account-b
                    print(f"The remaining balance in account ={c}")
                    break
            else:
                print("invalid choice")
        else:
            print("wrong password")
    else:
        print("enter correct card name---invalid")
"""
"""
while True:
    account = 100000
    pwd=1234
    card=input("insert card")
    if card=="c":
        print("welcome pooja")
        password=int(input("enter password"))

        if password==pwd:
              print("enter your option\n 1.Balance Enquiery: \n 2.Withdraw Amount: \n")
              option=int(input())
              if option==1:
                  print("your account balance is",account)
              elif option==2:
                    money=int(input("enter the amount"))
                    print(money)
                    balance=account-money
                    print("rem acc balance is",balance)
              else:
                    print("invalid option")
        else:
            print("enter correct password")
    else:
        print(" invalid card ")
"""        
                    
            
