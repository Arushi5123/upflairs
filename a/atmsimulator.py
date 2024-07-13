n=int(input("Enter the n:"))
for i in range (n):
    name=(input("Please enter your name:"))
    print("Hello",name)
    print("""How may I help you.

             Please select any of them option,
             Type 1 >>>> CHECK BALANCE.
             Type 2 >>>> DEPOSIT.
             Type 3 >>>> WITHDRAWL.""")
    available_amount=5000
    deposit_amount=0
    withdrawl_amount=0
    newavailable_amount=0
    deposit_amount=0
    task=int(input("Please enter your option:"))
    if(task>=1 and task<=3):
      if task==1:
        print("your balance is:",newavailable_amount)
      elif task==2:
        for j in range (n):
          deposit_amount=int(input("Please enter the amount to be deposited:"))
          if deposit_amount>500:
              available_amount+=deposit_amount
              print("you have successfully deposited your amount",deposit_amount)
              newavailable_amount=available_amount
              print("your available account is:",available_amount)
          else:
            print("dosto me uda do")
          newavailable_amount=available_amount
          newdeposit_amount=deposit_amount
      elif task==3:
        withdrawl_amount=int(input("Please enter amount to be withdrawl:"))
        if withdrawl_amount>newavailable_amount:
            y=(input("You don't have enough money, Do you want a loan?Please answer in yes and no:"))
            if y == "yes" :
                loan= withdrawl_amount-available_amount
                if newdeposit_amount==0 :
                    print("You have a loan of Rs:",loan)
                    available_amount=0
                    print("Your available amount is:",available_amount)
                else:
                    available_amount=0
                    available_amount+=newdeposit_amount
                    loan-=newdeposit_amount
                    print("Now your available amount is:",available_amount)
                    print("now your loan is:",loan)
            elif y =="no":
                print("Thankyou for visiting our virtual bank")
            elif y!="yes" and y!="no":
                print("Please answer in yes and no")
        else:
                available_amount-=withdrawl_amount
                print("Your withdrawl amount is:",withdrawl_amount)
                print("Your available amount is:",available_amount)
    else:
         print("Plese enter number either 1,2 or3")