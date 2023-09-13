fv=int(input("enter the Flip value :- "))

def Compute(a,b):
    y=lambda p,q,r:p*q*r
    if a==1:
        print(y(b,b,1))
    else:
        print(y(b,b,b))
        
if fv!=1 and fv!=2 :
    print("Invalid Input")
else:
    x=int(input("Enter the number :- "))
    Compute(fv,x)