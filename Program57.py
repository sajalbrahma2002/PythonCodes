N=int(input("Enter the amount to be deposited in the bank :- "))
M=int(input("Enter the time period in terms of years :- "))
Z=int(input("enter the interest on the amount per year :- "))

def Compute(a,b,c):
    x=lambda a,b,c:int((a*b*c)/100)
    print(x(a,b,c))

if N<=0 or M<=0 or Z<=0:
    print("Invalid Input")
else:
    Compute(N,M,Z)