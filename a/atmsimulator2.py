name=(input("Please enter your name:"))
print("Hello",name)
print("""How may I help you.

Please select any of them option,
Type 1 >>>> DEPOSIT.
Type 2 >>>> WITHDRAWL.
Type 3 >>>> CHECK BALANCE.""")
available_amount=5000
n=int(input())
task=int(input("Please enter your option:"))
if(task>=1 and task<=3):
    if task==1:
        deposit_amount=int(input("Please enter the amount to be deposited:"))
        if deposit_amount>500:
             available_amount+=deposit_amount
             print("you have successfully deposited your amount",deposit_amount)
             print("your available account is:",available_amount)
        else:
            print("dosto me uda do")
    elif task==2:
        withdrawl_amount=int(input("Please enter amount to be withdrawl:"))
        if withdrawl_amount>available_amount:
            y=(input("You don't have enough money, Do you want a loan?Please answer in yes and no:"))
            if y == "yes" :
                loan= withdrawl_amount-available_amount
                print("You have a loan of Rs:",loan)
                available_amount=0
                print("Your available amount is:",available_amount)
            elif y =="no":
                print("Thankyou for visiting our virtual bank")
            elif y!="yes" and y!=no:
                print("Please answer in yes and no")
        else:
                available_amount-=withdrawl_amount
                print("Your withdrawl amount is:",withdrawl_amount)
                print("Your available amount is:",available_amount)
    if task==3:
         print("your balance is:",available_amount)
      
else:
    print("Plese enter number either 1,2 or3")