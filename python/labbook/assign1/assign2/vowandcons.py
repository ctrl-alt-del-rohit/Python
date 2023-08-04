a=str(input("Enter the string: "))
vow_count=0
cons_count=0
for x in range(0,len(a)):
    if a[x] in ("a","e","i","o","u"):
        vow_count+=1
    elif (a[x] >= 'a' and a[x] <= 'z'):  
        cons_count+=1
print(vow_count)
print(cons_count)