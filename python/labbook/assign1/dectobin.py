def dectobin(a):
    if (a > 1):
        dectobin(a // 2)
        
    print(a % 2, end=" ")

a = int(input("Enter a number: "))
dectobin(a)