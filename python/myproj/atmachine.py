print("      ATM SERVICE")

Balance=2300
Deposit=0
Withdraw=0

print("Choose a number Corresponding to the Service")
while True:
    print("\n""1.Balance""\n""2.Deposit""\n""3.Withdraw")

    choice=int(input("Enter number:"))
    if choice==1:
        print("Balance: ₹",Balance)
    elif choice==2:
        cash_deposit=int(input("Enter Deposit Amount:"))
        Balance+=cash_deposit
        print("Amount Deposited")
        print("Updated Balance: ₹",Balance)
    elif choice==3:
        cash_withdraw=int(input("Enter Withdraw Amount:"))
        if cash_withdraw>Balance:
            print("You dont have enough balance!!")
        else:
            Balance-=cash_withdraw
            print("Amount Withdrawn: ₹",cash_withdraw)
            print("Updated Balance: ₹",Balance)
    elif choice==4:
        print("THANK YOU FOR USING OUR ATM SERVICE!!!!!")
        break
    else:
        print("***Choose only the number corresponding to the service***")

    

