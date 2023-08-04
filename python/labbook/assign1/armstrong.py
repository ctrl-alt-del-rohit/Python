num=1634
order=len(str(num))
xyz=0

temp=num

while temp>0:
    digit=temp%10
    xyz+=digit ** order
    temp //= 10
if num==xyz:
    print("armstrong")
else:
    print("non")