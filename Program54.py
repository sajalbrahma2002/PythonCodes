y=int(input("Enter the no of days to find the production of buses :- "))
def bus(a,b,c):
    if c>0:
        c=c-1
        x=a+b
        a=b
        b=x
        print(x,end=" ")
        bus(a,b,c)
if y<=0:
    print("Invalid Input")
elif y==1:
    print("1")
else:
    print("1 1",end=" ")
    bus(1,1,(y-2))