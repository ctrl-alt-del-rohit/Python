a=int(input("Enter a number:"))
temp=a
even_count=0
odd_count=0
zero_count=0
print("Original number",a)
while temp>0:
    digit=temp%10
    if digit==0:
        zero_count+=1
    elif digit%2==0:
        even_count+=1
    else:
        odd_count+=1
    temp//=10
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)
print("Zero :",zero_count)

