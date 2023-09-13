N=int(input("Enter the value of N:- "))
if N>0:
    smin=min=1000000
    for i in range (0,N):
        X=int(input("Enter a number :- "))
        if X<min:
            smin=min
            min=X
        elif X<smin:
            smin=X
    print("The second smallest number is  :- ",smin)
else:
    print("Invalid Input")