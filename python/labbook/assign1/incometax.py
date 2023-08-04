sal=int(input("Enter your salary in ₹:"))
if sal<250000:
    print("Below the minimum tax bracket.")
elif sal>250000 and sal<500000:
    tax=(sal*10)//100
    print("You are in 10% tax bracket.")
    print("Tax amount:",tax)
else:
    tax=(sal*20)//100
    print("You are in 20% tax bracket.")
    print("Tax amount:",tax)
