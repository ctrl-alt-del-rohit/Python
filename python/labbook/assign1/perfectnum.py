a=int(input("Enter the number"))
xyz=0

for x in range(1,a):
    if a % x == 0:
        xyz+= x

if xyz==a:
    print(f"{a} is a perfect number ")
else:
    print(f"{a} is not a perfect number")