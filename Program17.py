X1=int(input("Enter the trucks produced on day 1 :- "))
X2=int(input("Enter the trucks produced on day 2 :- "))
Y=int(input("Enter the no of days for the trucks to be produced :- "))
if Y>0:
    i=1
    while(i<=Y):
        print(X1,end=" ")
        sum=X1+X2
        X1=X2
        X2=sum
        i=i+1
else:
    print("Invalid Input")
