N=int(input("Enter the no of Apples bought :- "))
M=int(input("Enter the no of Bananas bought :- "))
Q=int(input("Enter the no of oranges bought :- "))
X=int(input("Enter the price of an Apple :- "))
Y=int(input("Enter the price of a Banana :- "))
Z=int(input("Enter the price of an Orange :- "))
sum=(N*X)+(M*Y)+(Q*Z)
if sum>0 and sum<=500:
    tax=((sum*2)/100)
    total=sum+tax
elif sum>500 and sum<=1000:
    tax=((sum*5)/100)
    total=sum+tax
else:
    tax=((sum*8)/100)
    total=sum+tax
print("The amount without tax added :- ",sum)
print("The tax added to the amount :- ",tax)
print("The amount to be paid after tax is :- ",total)