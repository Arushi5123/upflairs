name=input("Please enter your name:")
print("Hello",name)
message="""How may I help you.

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL."""
print(message)
task=int(input("please enter your option:"))
available_amount=5000 #constant amount in your account
if(task>=1 and task<=3):
    print("Welcome to you in our vitual bank")
    if task ==1:
        print("your available account is:",available_amount)
    elif task == 2:
        deposit_amount=int(input("please enter deposit amount:"))
        if deposit_amount>500:
           available_amount+=deposit_amount
           print("you have successfully deposited your amount",deposit_amount)
           print("your available account is:",available_amount)
            
        else:
           ("dosto me uta do")
    elif task ==3:
        withdrawl_amount=int(input("Enter the amount to be withdrawl"))
        if(withdrawl_amount>available_amount):
           print("you don't have enoung money")
        else:
           available_amount-=withdrawl_amount
           print("your withdrawl amount is",withdrawl_amount)
           print("your available account is:",available_amount)
                 
else:
    
    print("please select in between 1 to 3")
    
    
