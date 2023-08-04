num=int(input("Enter the digits: "))
temp=num
reverse=0
while temp > 0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp // 10
if num==reverse:
    print(f"The number {num} is a palindrome")
else:
    print(f"{num} is not a palindrome")