x=int(input("Enter the X co-ordinate"))
y=int(input("Enter the Y co-ordinate"))

print("(",x,",",y,")",end="")
if x>0 and y>0:
    print("Belongs to the 1st quadrant")
elif x>0 and y<0:
    print("Belongs to the 2nd quadrant")
elif x<0 and y<0:
    print("Belongs to the 3rd quadrant")
else:
    print("Belongs to the 4th quadrant")    
    