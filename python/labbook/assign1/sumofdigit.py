a=int(input("Enter the number: "))
temp=a
su=0
while temp>0:
    digit=temp%10
    su =su + digit
    temp//=10
print(f"Sum of the digits of {a} is",su)