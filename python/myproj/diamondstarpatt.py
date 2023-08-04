a=6
for x in range(a-1):
    for b in range(x,a):
        print(" ",end=" ")
    for y in range(x): 
        print("*",end=" ")
    for c in range(x+1): 
        print("*",end=" ")
    print()
for d in range(a):
    for e in range(d+1): 
        print(" ",end=" ")
    for f in range(d,a-1):
        print("*",end=" ")
    for g in range(d,a):
        print("*",end=" ")
    print()