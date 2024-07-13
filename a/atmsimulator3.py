name=int(input("enter your name"))
print("Hello",name)
meassage="""How may we help you?
            option1>>>check Balance
            option2>>>deposit
            option3>>>withdrarwl"""
n=int(input("enter your choice:"))
available_amount=10000
if n>=1 and n<=3:
    if n==1:
        print("You check balance is",available_amount)
    elif n==2:
        deposit_amount=int(input("enter the amount to be deposited:"))
        available_amount+=deposit_amount
        print("your balance is:",available_amount)
    elif n==3:
        withdrawl_amount=int(input("enter amount to be withdrawled"))
        if withdrawl_amount>available_amount:
            print("")
        
        
else:
    print("invalid choice")