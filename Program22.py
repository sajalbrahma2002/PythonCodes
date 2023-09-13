X=int(input("Enter the number :- "))
Y=int(input("Enter the value for the range of powers :- "))
if X>0 and Y>0:
    sum=0
    for i in range(0,Y):
        sum=sum+X**(i+1)
    print("The sum of powers of ",X," from 1 to ",Y," is :- ",sum)
else:
    print("Invalid Input")