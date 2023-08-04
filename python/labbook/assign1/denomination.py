amt=int(input("Enter the amount"))
print("=========================")
print("Amount withdrawn:",amt)
print("=========================")
ten=amt//10
amt=amt%10

five=amt//5
amt=amt%5

one=amt//1
amt=amt%1

print("10:",ten)
print("5:",five)
print("1:",one)
