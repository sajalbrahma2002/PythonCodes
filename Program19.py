N=int(input("Enter the value of N :- "))
if N>0:
    max=0
    for i in range (0,N):
        X=int(input("Enter a number :- "))
        if X>max:
            max=X
    print("Largest Number is :- ",max)
else:
    print("Invalid Input")