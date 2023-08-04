#Function for tables
def table(a,b):
    for x in range(1,a):
        print("***********************")
        for y in range(1,b):
            print(f"{x}x{y}= {x*y}")
#=============================================================
#Function for arithmetics
def arith(a,b):
    print("***********************")
    add=print(f"{a}+{b}={a+b}")
    print("***********************")
    substract=print(f"{a}-{b}={a-b}")
    print("***********************")
    multiply=print(f"{a}x{b}={a*b}")
    print("***********************")
    divide=print(f"{a}÷{b}={a/b}")
    print("***********************")
#=============================================================
#function for accepting a list
def urlist(list,integer):
    for x in range(0,integer):
        ele=int(input())
        list.append(ele)
#=============================================================       
#function for palindrome
def palin(a):
    reverse=0
    temp=a
    while temp > 0:
        remainder=temp%10
        reverse=(reverse*10)+remainder
        temp=temp // 10
    if a==reverse:
        print(f"The number {a} is a palindrome")
    else:
        print(f"{a} is not a palindrome")
    
#=============================================================       
#function for armstrong
def armstrong(a):
    cube=0
    temp=a
    items=len(str(a))
    while temp > 0:
        digit=temp%10
        cube+= digit** items
        temp //= 10
    if a==cube:
        print(f"{a} is an armstrong number")
    else:
        print(f"{a} is not an armstrong number")  

#=============================================================       
#function for perfect number
def perfect(a):
    divisor=0
    for x in range(1,a):
        if a%x==0:
            divisor+= x
    if divisor==a:
        print(f"{a} is a perfect number ")
    else:
        print(f"{a} is not a perfect number")

#=============================================================       
#function for sum of digits
def sumofdigits(a):
    temp=a
    summ=0
    while temp > 0:
        digit=temp % 10
        summ+= digit
        temp //= 10
    print(f"Sum of the digits of {a} is",summ)

#=============================================================       
#function for counting even odd and zero in a number
def count(a):
    temp=a
    even_count=0
    odd_count=0
    zero_count=0
    while temp>0:
        digit=temp%10
        if digit==0:
            zero_count+=1
        elif digit%2==0:
            even_count+=1
        else:
            odd_count+=1
        temp//=10
    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)
    print("Zero :",  zero_count) 
    
    
    
    
  