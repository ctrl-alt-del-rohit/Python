n=6
for x in range(n):
    for a in range(x+1,n+1):
        print(" ",end="  ")
    for z in range(1,x+1):
        print(z,end="  ")
    for y in range(x-1,0,-1):
        print(y,end="  ")
    print()
